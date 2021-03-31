from src.core.window import Window

class App:
    def __init__(self, window=None, title=None, size=(None, None), position=(None, None)):
        if window != None and isinstance(window, Window):
            self.window = window
        else:
            self.window = Window()
            
        if title != None:
            self.window.title(title)
            
        if size[0] != None and size[1] != None:
            self.window.resize(size[0], size[1])
        
        if position[0] != None and position[1] != None:
            self.window.relocate(position[0], position[1])
    
    def reset_window(self):
        self.window._reset_serialization()
    
    def run(self, deserialize=True):
        if deserialize:
            self.window._deserialize()
            
        self.window.run()