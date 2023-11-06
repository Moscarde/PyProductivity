import TKinterModernThemes as TKMT

def buttonCMD():
        print("Button clicked!")

class App(TKMT.ThemedTKinterFrame):
    def __init__(self):
        super().__init__("TITLE", "park", "dark")
        self.button_frame = self.addLabelFrame("Frame Label")
        self.button_frame.Button("Button Text", buttonCMD) #the button is dropped straight into the frame
        self.run()

App()