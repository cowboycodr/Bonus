from src.window import Window

class App:
    def __init__(self, window=None, title=None):
        if window != None and isinstance(window, Window):
            self.window = window
        else:
            self.window = Window()
            
        if title != None:
            self.window.window.title(title)
    
    def run(self):
        self.window.run()