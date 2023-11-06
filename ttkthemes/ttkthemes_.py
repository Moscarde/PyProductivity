from tkinter import *
from tkinter import ttk
from commands import open_output_folder
from ttkthemes import ThemedTk


def open_analysis_window():
    analysis_window = Toplevel()
    analysis_window.title("janela nova")
    analysis_window.geometry("800x600")
    label_nome = ttk.Label(analysis_window, text="Nome")
    label_nome.grid(row=0, column=0)
    botao_voltar = ttk.Button(
        analysis_window, text="Fechar janela", command=analysis_window.destroy
    )
    botao_voltar.grid(row=1, column=0)


root = ThemedTk(theme="scidpurple")  # yaru
root.geometry("300x400")

start_script_button = ttk.Button(root, text="Start Script")
start_script_button.place(relx=0.5, rely=0.5, anchor=CENTER)

open_output_folder_button = ttk.Button(
    root, text="Open Folder", command=open_output_folder
)
open_output_folder_button.place(relx=0.5, rely=0.6, anchor=CENTER)

data_analysis_button = ttk.Button(
    root, text="Data Analysis", command=open_analysis_window
)
data_analysis_button.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
