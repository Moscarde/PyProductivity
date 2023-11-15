import shutil, os
from tkinter import messagebox
from win32com.client import Dispatch

class FileHandler:
    @staticmethod
    def copy_to_startup():
        origin_path = "scripts/tracker.py"

        try:
            username = os.getenv("USERNAME")
            path = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\PyProductivity_tracker.lnk"
            # shutil.copy2(origin_path, path)

            shell = Dispatch('WScript.Shell')
            atalho = shell.CreateShortcut(path)
            atalho.TargetPath = os.path.abspath(origin_path)
            atalho.WorkingDirectory = os.path.dirname(os.path.abspath(origin_path))
            atalho.save()

            messagebox.showinfo(
                "Sucesso!", "O script foi adicionado ao início automático!"
            )
            messagebox.showinfo("Caminho", path)
        except Exception as error:
            messagebox.showerror("Erro ao adicionar ao início automático!", error)





        # def criar_atalho(arquivo_origem, atalho_destino):
        #     shell = Dispatch('WScript.Shell')
        #     atalho = shell.CreateShortcut(atalho_destino)
        #     atalho.TargetPath = os.path.abspath(arquivo_origem)
        #     atalho.WorkingDirectory = os.path.dirname(os.path.abspath(arquivo_origem))
        #     atalho.save()

        # arquivo_origem = "script/tracker.py"
        # atalho_destino = path

        # criar_atalho(arquivo_origem, atalho_destino)

    @staticmethod
    def load_logs_filenames():
        files = os.listdir("logs/")
        csv_files = [file for file in files if file.endswith(".csv")]
        return csv_files