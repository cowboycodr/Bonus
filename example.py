from src.core.app import App
from src.core.window import Window

class ExampleWindow(Window):
    def __init__(self):
        super().__init__()
        
if __name__ == '__main__':
    app = App(ExampleWindow())
    app.window.center()
    app.run()
    
    # remove this code if you would like the application to save the size and location of the window
    app.reset_window()