from src.app import App
from src.window import Window

class BonusWindow(Window):
    def __init__(self):
        super().__init__()
        
if __name__ == '__main__':
    app = App(BonusWindow())
    app.window.center(resize=True, size_hint_width=1, size_hint_height=1, pos_hint_x=2, pos_hint_y=0)
    app.run()