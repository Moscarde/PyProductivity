import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import os
from modules.report import get_df_report
from modules.tracker import start_tracker

root = tk.Tk()
root.title("Grafic Plot")
root.geometry("200x400")
csv_list = []

def open_analysis_window():
    analysis_window = tk.Toplevel()
    analysis_window.title('janela nova')
    analysis_window.geometry("1000x600")

    my_button2 = tk.Button(analysis_window, text="Mostrar csvs", command=show_csvs_paths())
    my_button2.pack()

    # Label Frame Para o Grafico
    labelframe = tk.LabelFrame(analysis_window, text="Tempo de uso do dia")
    labelframe.pack(fill="both", expand="yes")

    def plot_graph(event, labelframe = labelframe):
        # processa o arquivo csv
        filename = event.widget.get()
        csv_path = f"{os.getcwd()}\logs\{filename}"
        df = get_df_report(csv_path)

        # Cria uma figura Matplotlib
        fig, ax = plt.subplots()
        ax.bar(df["app_name"].head(5), df["daily_usage"].head(5))

        # Limpa os itens dentro do labelframe
        clear_label_frame(labelframe)

        # Adiciona o gráfico à janela Tkinter
        canvas = FigureCanvasTkAgg(fig, master=labelframe)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    # Select csv
    select_csv = ttk.Combobox(analysis_window, values=csv_list)
    select_csv.set("Pick an Option")
    select_csv.pack(padx=5, pady=5)
    select_csv.current()
    select_csv.bind("<<ComboboxSelected>>", plot_graph)


def clear_label_frame(labelframe):
    # Limpa todos os widgets dentro do Labelframe
    for widget in labelframe.winfo_children():
        widget.destroy()


def show_csvs_paths():
    # retorna a lista de arquivos csv
    global csv_list
    files = os.listdir("logs/")
    csv_files = [file for file in files if file.endswith(".csv")]
    csv_list = csv_files


# TkInter Elementos
# Botao Mostrar graficos

# Botao Mostrar csvs
start_tracker_button = ttk.Button(root, text="Iniciar Monitoramento", command=start_tracker)
start_tracker_button.pack()

analysis_button = ttk.Button(root, text="Analisar relatórios", command=open_analysis_window)
analysis_button.pack()

def on_close():
    root.quit()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
