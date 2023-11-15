import tkinter as tk
import win32con
import win32gui
from view.main_interface import MainInterface


def on_close(root):
    root.quit()
    root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainInterface(root)

    root.protocol("WM_DELETE_WINDOW", lambda: on_close(root))
    root.mainloop()
