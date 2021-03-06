from src.uix.layouts.parser.buttonparser import ButtonParser
from src.uix.layouts.parser.labelparser import LabelParser

class Layout:
    def __init__(self, app, *widgets):
        self.window = app.window
        self.size = self.window.size
        
        self.widget_types = [
            'button',
            'label'
        ]
        
        self.widgets = []
        
        for widget in widgets:
            self.add_widget(widget)
        
    def add_widget(self, widget):
        if widget.kind not in self.widget_types:
            raise Exception(f'Widget type: {widget.kind}: is not supported')
        
        self.widget_protocol(widget)
        
        if widget.kind == 'button':
            self.widgets.append(
                ButtonParser(widget).result()
            )
        elif widget.kind == 'label':
            self.widgets.append(
                LabelParser(widget).result()
            )    
        
    def widget_protocol(self, widget):
        '''
        add layout specific widget transformations here
        '''
        pass