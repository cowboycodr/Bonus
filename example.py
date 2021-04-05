from src.core.app import App
from src.core.window import Window
import time

import os
class ExampleWindow(Window):
    def __init__(self):
        super().__init__()
        
        # updates per second, default FPS is 60, do not rely on it being 100% accurate
        self.FPS = 500
        
        self.start = time.time()
        
    # gets called everytime the window updates
    def update(self, changes):
        self.title(self.current_frame_rate())
        
    def on_close(self, window):
        print(self.frame_count / round(time.time() - self.start))
    
if __name__ == '__main__':
    app = App(ExampleWindow())
    app.window.center()
    app.run()
    
    appWindow = app.window
    print(appWindow)
    
    # remove this code if you would like the application to save the size and location of the window when closed
    app.reset_window()