
class App:
    def __init__(self, state = None, gui = None):
        self.state = state
        self.gui = gui
    
    def exit(self):
        self.gui.close()


app = App()
