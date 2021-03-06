from src.core.window import Window

class App:
    def __init__(self, window=None, title=None, size=(None, None), position=(None, None), deserialize=True):
        if window != None and isinstance(window, Window):
            self.window = window
        else:
            self.window = Window()
            
        if deserialize:
            try:
                self.window._deserialize()
            except:
                self.window._serialize()
        
        if title != None:
            self.window.title(title)
            
        if size[0] != None and size[1] != None:
            self.window.resize(size[0], size[1])
        
        if position[0] != None and position[1] != None:
            self.window.relocate(position[0], position[1])
    
    def __repr__(self):
        return '{self.__class__.__name__}(window={self.window}, title={self.window.window_title}, size={self.window.size}, position={self.window.position})'.format(self=self)
    
    def reset_window(self):
        self.window._reset_serialization()
        
        if self.window.running:
            self.window._deserialize()
    
    def run(self, deserialize=True):
        self.window.run()