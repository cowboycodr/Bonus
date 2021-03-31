from src.core.app import App
from src.core.window import Window
from src.core.widgets.button import Button

class CarWindow(Window):
    def __init__(self):
        super().__init__()
        
if __name__ == '__main__':
    app = App(CarWindow())
    app.run()