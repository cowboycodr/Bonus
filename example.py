from src.core.app import App
from src.core.window import Window

class BonusWindow(Window):
    def __init__(self):
        super().__init__()
        
if __name__ == '__main__':
    app = App(BonusWindow())
    app.run()