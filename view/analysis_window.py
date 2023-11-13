import tkinter as tk
from tkinter import ttk
import os
from modules.report import get_df_report
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

csv_list = []


def open_analysis_window():
    analysis_window = tk.Toplevel()
    analysis_window.title("janela nova")
    analysis_window.geometry("1000x600")

    load_csvs_paths()
    # Select csv
    def on_combo_change(event):
        plot_graph(event, labelframe)

    select_csv = ttk.Combobox(analysis_window, values=csv_list)
    select_csv.set("Pick an Option")
    select_csv.pack(padx=5, pady=5)
    select_csv.current()
    select_csv.bind("<<ComboboxSelected>>", on_combo_change)

    # Label Frame Para o Grafico
    labelframe = tk.LabelFrame(analysis_window, text="Tempo de uso do dia")
    labelframe.pack(fill="both", expand="yes")

    

    


def plot_graph(event, labelframe):
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


def clear_label_frame(labelframe):
    # Limpa todos os widgets dentro do Labelframe
    for widget in labelframe.winfo_children():
        widget.destroy()


def load_csvs_paths():
    # retorna a lista de arquivos csv
    global csv_list
    files = os.listdir("logs/")
    csv_files = [file for file in files if file.endswith(".csv")]
    return csv_files
    
