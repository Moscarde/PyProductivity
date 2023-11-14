import datetime
import os
import shutil
import subprocess
import tkinter as tk
import webbrowser
from tkinter import filedialog, messagebox, ttk

import matplotlib.cbook as cbook
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
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


class Menu:
    @staticmethod
    def open_logs_folder():
        path = os.path.join(os.getcwd(), "logs")
        webbrowser.open(path)

    @staticmethod
    def open_startup_folder():
        username = os.getenv("USERNAME")
        path = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
        webbrowser.open(path)

    @staticmethod
    def open_repository_readme():
        webbrowser.open("https://github.com/moscarde/PyProductivity")

    @staticmethod
    def open_repository_issue():
        webbrowser.open("https://github.com/Moscarde/PyProductivity/issues")


class MainInterface:
    def __init__(self, root):
        self.root = root
        self.configure_interface()
        self.configure_menu()

        self.image = tk.PhotoImage(file="pictures/small_logo.png")
        self.label = tk.Label(root, image=self.image, width=250, height=85)
        self.label.place(x=10, y=10)

        self.button_open_script = self.create_button(
            "Iniciar Monitoramento", command=self.open_script, x=10, y=110
        )

        self.button_open_analysis_window = self.create_button(
            "Analisar relatórios", command=self.open_analysis_window, x=10, y=145
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

    def configure_menu(self):
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        self.shortcuts = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Abrir", menu=self.shortcuts)
        self.shortcuts.add_command(
            label="Abrir pasta de logs", command=Menu.open_logs_folder
        )
        self.shortcuts.add_command(
            label="Abrir pasta de início automático", command=Menu.open_startup_folder
        )
        self.shortcuts.add_separator()
        self.shortcuts.add_command(label="Fechar aplicação", command=self.root.destroy)

        self.about = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Sobre", menu=self.about)
        self.about.add_command(
            label="Reporte um problema", command=Menu.open_repository_issue
        )
        self.about.add_command(
            label="Repositório PyProductivity", command=Menu.open_repository_readme
        )

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

        self.image_path = cbook.get_sample_data(
            os.path.join(os.getcwd(), "pictures", "bg_graph.jpg")
        )

        self.img = plt.imread(self.image_path)
        self.fig.set_facecolor(Constants.BG_COLOR)
        # self.ax.imshow(self.img, extent=[-1, 5, 0, 6], aspect="auto")

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.parent_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update_graph(self, df, options):
        self.df = df.head(options["qtd_apps"])
        self.y_lim = self.df["daily_usage_seconds"].max()
        if self.y_lim > 600:
            self.y_lim = self.y_lim * 1.15
        else:
            self.y_lim = 900

        self.setup_axes(options)
        self.plot_background_image(options)
        self.bars = self.plot_bars(self.df)
        self.configure_y_ticks(self.df["daily_usage_seconds"].max())
        self.configure_x_ticks()
        self.add_value_labels(self.bars)
        self.canvas.draw()

    def setup_axes(self, options):
        self.ax.clear()
        self.ax.set_title(self.parse_date(options["Date"]))
        self.ax.set_ylabel("Tempo de Uso", fontsize=16)
        self.ax.set_xlabel("Programas", fontsize=16)

    def parse_date(self, date):
        weekday_list_pt_br = [
            "Segunda-feira",
            "Terça-feira",
            "Quarta-feira",
            "Quinta-feira",
            "Sexta-feira",
            "Sábado",
            "Domingo",
        ]
        datetime_obj = datetime.datetime.strptime(date.split(".")[0], "%Y-%m-%d")
        weekday = weekday_list_pt_br[datetime_obj.weekday()]
        return f'{weekday} - {datetime_obj.strftime(f"%d/%m/%Y")}'

    def plot_background_image(self, options):
        self.ax.imshow(
            self.img, extent=[-0.7, options["qtd_apps"], 0, self.y_lim], aspect="auto"
        )

    def plot_bars(self, df):
        bars = self.ax.bar(
            df["app_name"],
            df["daily_usage_seconds"],
            color=Constants.BUTTON_ACTIVE_COLOR,
        )
        return bars

    def configure_y_ticks(self, max_value):
        self.ax.yaxis.set_major_formatter(ticker.FuncFormatter(self.format_hours))

        rounded_max_value = np.ceil(max_value / 900) * 900
        num_ticks = 5
        tick_interval = rounded_max_value / (num_ticks - 1)
        desired_ticks = [i * tick_interval for i in range(num_ticks)]
        self.ax.set_yticks(desired_ticks)

    def configure_x_ticks(self):
        formated_labels = [
            self.limit_text(label.get_text()) for label in self.ax.get_xticklabels()
        ]
        self.ax.set_xticks(self.ax.get_xticks())
        self.ax.set_xticklabels(formated_labels)

    def limit_text(self, text):
        max_length = 18
        if len(text) > max_length:
            return text[: max_length - 3] + "..."
        else:
            return text

    def add_value_labels(self, bars):
        for bar in bars:
            yval = bar.get_height()
            self.ax.text(
                bar.get_x() + bar.get_width() / 2,
                yval,
                self.format_hours(yval, 0),
                ha="center",
                va="bottom",
                color="black",
                fontsize=9,
            )

    def format_hours(self, x, _):
        hours = int(x // 3600)
        minutes = int((x % 3600) // 60)
        if hours == 0:
            return f"{minutes:02d}m"
        elif minutes == 0:
            return f"{hours:02d}h"
        else:
            return f"{hours:02d}h {minutes:02d}m"


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
