import os
import tkinter as tk
from tkinter import filedialog, ttk

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

from modules.report import get_df_report
from modules.tracker import start_tracker
from view.analysis_window import open_analysis_window

root = tk.Tk()
root.title("Grafic Plot")
root.geometry("275x205")
root.configure(bg="#E6E6FA")


# TkInter Elementos
# Botao Mostrar graficos

image = tk.PhotoImage(file="pictures/small_logo.png")
label = tk.Label(root, image=image, width=250, height=85)
label.place(x=10, y=10)

# Botao Mostrar csvs
start_tracker_button = tk.Button(
    root,
    text="Iniciar Monitoramento",
    command=start_tracker,
    width=35,
    background="#cbc3e3",
    activebackground="#603ffe",
)
start_tracker_button.place(x=10, y=110)
# tk.Label(root, text="Position 1 : x=0, y=0", bg="#FFFF00", fg="black").place(x=5, y=0)

analysis_button = tk.Button(
    root,
    text="Analisar relatórios",
    command=open_analysis_window,
    width=35,
    background="#cbc3e3",
    activebackground="#603ffe",
)
analysis_button.place(x=10, y=150)


def on_close():
    root.quit()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
