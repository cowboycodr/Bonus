class Layout:
    def __init__(self, app, *widgets):
        self.window = app.window
        self.size = self.window.size
        
        self.widget_types = [
            'button'
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
                [
                    'button',
                    {
                        'activebackground' : widget.activebackground,
                        'activeforeground' : widget.activeforeground,
                        'bd' : widget.bd,
                        'bg' : widget.bg,
                        'command' : widget.command,
                        'fg' : widget.fg,
                        'font' : widget.font,
                        'height' : widget.height,
                        'highlightcolor' : widget.highlightcolor,
                        'image' : widget.image,
                        'justify' : widget.justify,
                        'padx' : widget.padx,
                        'pady' : widget.pady,
                        'relief' : widget.relief,
                        'state' : widget.state,
                        'text' : widget.text,
                        'underline' : widget.underline,
                        'width' : widget.width,
                        'wraplength' : widget.wraplength
                    }
                ]
            )
            
    def widget_protocol(self, widget):
        '''
        add layout specific widget transformations here
        '''
        pass