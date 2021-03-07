from src.app import App
from src.uix.layouts.layout import Layout
from src.uix.widgets.button import Button
from src.uix.widgets.label import Label

class Polaris(App):
    def __init__(self):
        super().__init__(
            title='Polaris'
        )
        
    
    def build(self):
        l = Layout(self)
        l.add_widget(Button(text='Button'))
        l.add_widget(Label(text='label working?'))
        return l
    
if __name__ == '__main__':
    Polaris().run()