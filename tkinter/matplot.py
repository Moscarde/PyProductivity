import TKinterModernThemes as TKMT
import random

class App(TKMT.ThemedTKinterFrame):
    def __init__(self): 
        super().__init__("Matplotlib Example")

        self.graphframe = self.addLabelFrame("2D Graph")
        self.graphframe2 = self.addLabelFrame("3D Graph", col=1)
        self.canvas, fig, self.ax, background, self.accent = self.graphframe.matplotlibFrame("Graph Frame Test")
        self.canvas2, fig2, self.ax2, _, _ = self.graphframe2.matplotlibFrame("Graph 3D", projection='3d')
        buttonframe = self.addLabelFrame("Control Buttons", colspan=2)
        buttonframe.Button("Add Data", self.addData)
        self.run()

    def addData(self):
        x = []
        y = []
        z = []

        for i in range(0, 100):
            for l in [x, y, z]:
                l.append(random.random() * 100)

        self.ax.scatter(x, y, c=self.accent)
        self.ax2.scatter(x, y, z, c=self.accent)
        self.canvas.draw()
        self.canvas2.draw()

if __name__ == "__main__":
    App()