from tkinter import Button as TkinterButton

class Button:
    def __init__(self, window, bg=None, fg=None, command=None, text=None, font=None, height=None, width=None, image=None, anchor='center'):
        self.window = window
        self.bg = bg
        self.fg = fg
        self.command = command
        self.text = text
        self.font = font
        self.height = height
        self.width = width
        self.image = image
        
        self.anchor = anchor
        
        self.button = TkinterButton(master=self.window, text=self.text, bg=self.bg, fg=self.fg, command=self.command, font=self.font, height=self.height, width=self.width, image=self.image)
        
        self.button.pack(anchor=self.anchor)