class LabelParser:
    def __init__(self, widget):
        self.label = [
            'label',
            {
                'anchor' : widget.anchor,
                'bg' : widget.bg,
                'bitmap' : widget.bitmap,
                'bd' : widget.bd,
                'cursor' : widget.cursor,
                'font' : widget.font,
                'fg' : widget.fg,
                'height' : widget.height,
                'image' : widget.image,
                'justify' : widget.justify,
                'padx' : widget.padx,
                'pady' : widget.pady,
                'relief' : widget.relief,
                'text' : widget.text,
                'textvariable' : widget.textvariable,
                'underline' : widget.underline,
                'width' : widget.underline,
                'wraplength' : widget.wraplength
            }
        ]
        
    def result(self):
        return self.label