from model.file_handler import FileHandler
from model.data_handler import DataHandler
from tkinter import ttk
from constants import Constants
import tkinter as tk
from view.graph import Graph
import os

class AnalysisInterface:
    def __init__(self, root):
        self.root = root
        self.analysis_interface = tk.Toplevel(root)
        self.configure_interface()

        self.csv_list = FileHandler.load_logs_filenames()

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
        df = DataHandler.usage_time_acum(csv_path)

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
