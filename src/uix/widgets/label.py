'''
The label widget provides simple access to Tkinter's 
label. The arguments are the same as Tkinter's and 
the only difference is certain layouts can change 
the size and position of this label. 
'''

class Label:
    def __init__(self, anchor=None, bg=None, bitmap=None, bd=None, cursor=None, font=None, fg=None, height=None, image=None, justify=None, padx=None, pady=None, relief=None, size_hint=(1,1), text=None, textvariable=None, underline=None, width=None, wraplength=None):
        
        # Values handles by Tkinter
        self.anchor = anchor
        self.bg = bg
        self.bitmap = bitmap
        self.bd = bd
        self.cursor = cursor
        self.font = font
        self.fg = fg
        self.image = image
        self.justify = justify
        self.padx = padx
        self.pady = pady
        self.relief = relief
        self.text = text
        self.textvariable = textvariable
        self.underline = underline
        self.wraplength = wraplength
        
        # Values handled by Bonus
        self.height = height
        self.kind = 'label'
        self.size_hint = size_hint
        self.width = width
        
    def config(self, anchor=None, bg=None, bitmap=None, bd=None, cursor=None, font=None, fg=None, height=None, image=None, justify=None, padx=None, pady=None, relief=None, size_hint=(1,1), text=None, textvariable=None, underline=None, width=None, wraplength=None):
        self.__init__(
            anchor, 
            bg,
            bitmap,
            bd,
            cursor,
            font,
            fg,
            height,
            image,
            justify,
            padx,
            pady,
            relief,
            size_hint,
            text,
            textvariable,
            underline,
            width,
            wraplength
        )