class ButtonParser:
    def __init__(self, widget):
        self.button = [
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
        
    def result(self):
        return self.button