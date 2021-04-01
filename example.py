from src.core.app import App
from src.core.window import Window

class ExampleWindow(Window):
    def __init__(self):
        super().__init__()
        
        # updates per second, default FPS is 60, do not rely on it being 100% accurate
        self.FPS = 60
        
        self.window_title = 0
        
    def update(self, changes):
        self.window_title += 1
        self.title(self.window_title)
    
if __name__ == '__main__':
    app = App(ExampleWindow())
    app.window.center()
    app.run()
    
    # remove this code if you would like the application to save the size and location of the window when closed
    app.reset_window()