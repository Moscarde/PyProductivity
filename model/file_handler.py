import shutil, os
from tkinter import messagebox
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

    @staticmethod
    def load_logs_filenames():
        files = os.listdir("logs/")
        csv_files = [file for file in files if file.endswith(".csv")]
        return csv_files