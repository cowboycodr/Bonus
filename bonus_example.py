from src.app import App
from src.uix.layouts.layout import Layout
from src.uix.widgets.button import Button

class Polaris(App):
    def __init__(self):
        super().__init__(
            title='Polaris'
        )
        
    def build(self):
        return Layout(self, Button(text='Bonus'))
    
if __name__ == '__main__':
    Polaris().run()