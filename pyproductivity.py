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
import subprocess
import win32gui, win32con
import shutil

root = tk.Tk()
root.title("Grafic Plot")
root.geometry("275x205")
root.configure(bg="#E6E6FA")

# hide main console
# hide = win32gui.GetForegroundWindow()
# win32gui.ShowWindow(hide , win32con.SW_HIDE)
def add_to_startup():
    origin_path = 'modules/tracker.py'
    path = 'C:\\Users\\Gabriel\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\tracker.py'
    shutil.copy2(origin_path, path)


def open_script():
    subprocess.Popen(['start', 'cmd', '/k', 'python', 'modules/tracker.py'], shell=True)


# TkInter Elementos
# Botao Mostrar graficos

image = tk.PhotoImage(file="pictures/small_logo.png")
label = tk.Label(root, image=image, width=250, height=85)
label.place(x=10, y=10)

# Botao Mostrar csvs
start_tracker_button = tk.Button(
    root,
    text="Iniciar Monitoramento",
    command=open_script,
    # command=start_tracker,
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

add_to_startup_button = tk.Button(
    root,
    text="Teste terminal",
    command=add_to_startup,
    width=35,
    background="#cbc3e3",
    activebackground="#603ffe",
)
add_to_startup_button.place(x=10, y=180)


def on_close():
    root.quit()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
