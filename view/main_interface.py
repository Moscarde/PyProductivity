import tkinter as tk
import subprocess
from model.file_handler import FileHandler
from constants import Constants
from view.menu import Menu
from view.analysis_interface import AnalysisInterface

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
