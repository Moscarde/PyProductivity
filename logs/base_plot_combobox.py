import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import os
from get_df_report import get_df_report

root = tk.Tk()
root.title("Grafic Plot")
root.geometry("1000x600")
csv_list = []


def plot_graph(event):
    # processa o arquivo csv
    filename = event.widget.get()
    csv_path = f"{os.getcwd()}\logs\{filename}"
    df = get_df_report(csv_path)

    # Cria uma figura Matplotlib
    fig, ax = plt.subplots()
    ax.bar(df["app_name"].head(5), df["daily_usage"].head(5))

    # Limpa os itens dentro do labelframe
    clear_label_frame()

    # Adiciona o gráfico à janela Tkinter
    canvas = FigureCanvasTkAgg(fig, master=labelframe)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Adiciona barra de rolagem, se necessário
    scrollbar = tk.Scrollbar(root, command=canvas.get_tk_widget().yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.get_tk_widget().config(yscrollcommand=scrollbar.set)


def clear_label_frame():
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
my_button2 = tk.Button(root, text="Mostrar csvs", command=show_csvs_paths())
my_button2.pack()

# Select csv
select_csv = ttk.Combobox(root, values=csv_list)
select_csv.set("Pick an Option")
select_csv.pack(padx=5, pady=5)
select_csv.current()
select_csv.bind("<<ComboboxSelected>>", plot_graph)

# Label Frame Para o Grafico
labelframe = tk.LabelFrame(root, text="Tempo de uso do dia")
labelframe.pack(fill="both", expand="yes")


def on_close():
    root.quit()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
