import os, webbrowser
class Menu:
    @staticmethod
    def open_logs_folder():
        path = os.path.join(os.getcwd(), "logs")
        webbrowser.open(path)

    @staticmethod
    def open_startup_folder():
        username = os.getenv("USERNAME")
        path = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
        webbrowser.open(path)

    @staticmethod
    def open_repository_readme():
        webbrowser.open("https://github.com/moscarde/PyProductivity")

    @staticmethod
    def open_repository_issue():
        webbrowser.open("https://github.com/Moscarde/PyProductivity/issues")
