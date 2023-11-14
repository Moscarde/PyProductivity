import os
import shutil
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import matplotlib.cbook as cbook
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import win32con
import win32gui
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

from modules.report import get_df_report
from view.analysis_window import load_csvs_paths, open_analysis_window


class Constants:
    BG_COLOR = "#E6E6FA"
    BUTTON_COLOR = "#CBC3E3"
    BUTTON_ACTIVE_COLOR = "#603FFE"


class FileHandler:
    @staticmethod
    def copy_to_startup():
        origin_path = "modules/tracker.py"

        try:
            username = os.getenv("USERNAME")
            path = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\PyProductivity_tracker.py"
            shutil.copy2(origin_path, path)

            messagebox.showinfo(
                "Sucesso!", "O script foi adicionado ao início automático!"
            )
            messagebox.showinfo("Caminho", path)
        except Exception as error:
            messagebox.showerror("Erro ao adicionar ao início automático!", error)


class MainInterface:
    def __init__(self, root):
        self.root = root
        self.configure_interface()

        self.image = tk.PhotoImage(file="pictures/small_logo.png")
        self.label = tk.Label(root, image=self.image, width=250, height=85)
        self.label.place(x=10, y=10)

        self.button_open_script = self.create_button(
            "Iniciar Monitoramento", command=self.open_script, x=10, y=110
        )

        self.button_open_analysis_window = self.create_button(
            "Analisar relatórios", command=self.open_analysis_window, x=10, y=150
        )

        self.button_add_to_startup = self.create_button(
            "Adicionar ao início automático",
            command=FileHandler.copy_to_startup,
            x=10,
            y=180,
        )

    def configure_interface(self):
        self.root.title("PyProductivity")
        self.root.geometry("275x215")
        self.root.configure(bg=Constants.BG_COLOR)

    def create_button(self, text, command, x, y):
        return tk.Button(
            self.root,
            text=text,
            command=command,
            width=35,
            background=Constants.BUTTON_COLOR,
            activebackground=Constants.BUTTON_ACTIVE_COLOR,
        ).place(x=x, y=y)

    def open_script(self):
        subprocess.Popen(
            ["start", "cmd", "/k", "python", "modules/tracker.py"], shell=True
        )

    def open_analysis_window(self):
        AnalysisInterface(self.root)


class Graph:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.fig, self.ax = plt.subplots()

        self.image_path = cbook.get_sample_data(os.path.join(os.getcwd(), "pictures", "bg_graph2.jpg"))

        self.img = plt.imread(self.image_path)
        self.fig.set_facecolor(Constants.BG_COLOR)
        self.ax.imshow(self.img, extent=[-1, 5, 0, 6], aspect="auto")

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.parent_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update_graph(self, df, options):
        self.ax.clear()

        self.y_lim = df["daily_usage"].max() + 1
        self.x_lim = options["qtd_apps"]
        self.ax.imshow(self.img, extent=[-1, self.x_lim, 0, self.y_lim], aspect="auto")

        self.ax.set_title(options["Date"])
        self.ax.set_ylabel("Horas")
        self.ax.set_xlabel("Programas")

        self.bars = self.ax.bar(
            df["app_name"].head(options["qtd_apps"]),
            df["daily_usage"].head(options["qtd_apps"]),
            color=Constants.BUTTON_ACTIVE_COLOR,
        )

        self.ax.grid(options["grid_enables"])
        for bar in self.bars:
            yval = bar.get_height()
            self.ax.text(
                bar.get_x() + bar.get_width() / 2,
                yval,
                round(yval, 2),
                ha="center",
                va="bottom",
                color="black",
                fontsize=9,
            )

        self.canvas.draw()


class AnalysisInterface:
    def __init__(self, root):
        self.root = root
        self.analysis_interface = tk.Toplevel(root)
        self.configure_interface()

        self.csv_list = load_csvs_paths()

        self.combo_csv = ttk.Combobox(
            self.analysis_interface, values=self.csv_list, width=35
        )
        self.combo_csv.set("Pick an Option")
        self.combo_csv.pack(padx=5, pady=5)
        self.combo_csv.current()
        self.combo_csv.bind("<<ComboboxSelected>>", self.on_combo_change)

        # Label Frame Para o Grafico
        self.labelframe = tk.LabelFrame(
            self.analysis_interface, text="Tempo de uso do dia", bg=Constants.BG_COLOR
        )
        self.labelframe.pack(fill="both", expand="yes", padx=5, pady=5)
        self.graph = Graph(self.labelframe)

        if len(self.csv_list) > 0:
            self.combo_csv.set(self.csv_list[-1])
            self.on_combo_change(None)
        else:
            self.combo_csv.set("Nenhum relatório encontrado")

    def configure_interface(self):
        self.analysis_interface.title("Segunda Interface")
        self.analysis_interface.geometry("1000x600")
        self.analysis_interface.configure(bg=Constants.BG_COLOR)

    def load_csvs_paths(self):
        self.files = os.listdir("logs/")
        self.csv_files = [file for file in self.files if file.endswith(".csv")]
        return self.csv_files

    def on_combo_change(self, event):
        if event == None:
            filename = self.combo_csv.get()
        else:
            filename = event.widget.get()

        csv_path = os.path.join(os.getcwd(), "logs", filename)
        df = get_df_report(csv_path)

        options = {
            "qtd_apps": 5,
            "grid_enables": False,
            "Date": filename,
        }
        self.graph.update_graph(df, options)

    def clear_label_frame(self, labelframe):
        # Limpa todos os widgets dentro do Labelframe
        for widget in labelframe.winfo_children():
            widget.destroy()


def on_close(root):
    root.quit()
    root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainInterface(root)

    root.protocol("WM_DELETE_WINDOW", lambda: on_close(root))
    root.mainloop()
