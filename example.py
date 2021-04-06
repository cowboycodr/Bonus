from src.core.app import App
from src.core.window import Window
import time
import os

class ExampleWindow(Window):
    def __init__(self):
        super().__init__()
        
        # updates per second, default FPS is 60
        self.FPS = 60
        
        self.start = time.time()
    
    # gets called everytime the window updates
    def update(self, changes):
        self.title(self.avg_frame_rate())
    
if __name__ == '__main__':
    app = App(ExampleWindow())
    app.window.resize(1920, 1080)
    app.window.center(resize=True, size_hint_width=1.25, size_hint_height=1.7)
    app.run()
    
    appWindow = app.window
    print(appWindow)
    print(app)
    
    # remove this code if you would like the application to save the size and location of the window when closed
    # app.reset_window()