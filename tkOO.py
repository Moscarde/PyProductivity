import tkinter as tk

class InterfacePrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface Principal")

        self.label = tk.Label(root, text="Interface Principal")
        self.label.pack(pady=10)

        self.botao = tk.Button(root, text="Abrir Segunda Interface", command=self.abrir_segunda_interface)
        self.botao.pack(pady=10)

    def abrir_segunda_interface(self):
        segunda_interface = InterfaceSecundaria(self.root)

class InterfaceSecundaria:
    def __init__(self, root):
        self.root = root
        self.top_level = tk.Toplevel(root)
        self.top_level.title("Segunda Interface")

        self.label = tk.Label(self.top_level, text="Segunda Interface")
        self.label.pack(pady=10)

# Inicialização da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfacePrincipal(root)
    root.mainloop()
