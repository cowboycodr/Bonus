class Button:
    def __init__(self, activebackground=None, activeforeground=None, bd=None, bg=None, command=None, fg=None, font=None, height=None, highlightcolor=None, image=None, justify=None, padx=None, pady=None, relief=None, state=None, size_hint=(1, 1), text=None, underline=None, width=None, wraplength=None):
        
        # Values handled by Tkinter
        self.activebackground = activebackground
        self.activeforeground = activeforeground
        self.bd = bd
        self.bg = bg
        self.command = command
        self.fg = fg
        self.font = font
        self.highlightcolor = highlightcolor
        self.image = image
        self.justify = justify
        self.padx = padx
        self.pady = pady
        self.relief = relief
        self.state = state
        self.text = text
        self.underline = underline
        self.wraplength = wraplength
        
        # Values handled by Bonus
        self.height = height
        self.kind = 'button'
        self.size_hint = size_hint
        self.width = width
        
    def config(self, activebackground=None, activeforeground=None, bd=None, bg=None, command=None, fg=None, font=None, height=None, highlightcolor=None, image=None, justify=None, padx=None, pady=None, relief=None, state=None, size_hint=(1, 1), text=None, underline=None, width=None, wraplength=None):
        
        self.__init__(
            activebackground,
            activeforeground,
            bd,
            bg,
            command,
            fg,
            font,
            height,
            highlightcolor,
            image,
            justify,
            padx,
            pady,
            relief,
            state,
            size_hint,
            text,
            underline,
            width,
            wraplength
        )