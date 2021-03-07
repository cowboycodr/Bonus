from tkinter import Button as TkinterButton
from tkinter import Label as TkinterLabel

def button(app, widget):
    widget = widget[1]
    
    button = TkinterButton(
            master=app.window,
            activebackground=widget['activebackground'],
            activeforeground=widget['activeforeground'],
            bd=widget['bd'],
            bg=widget['bg'],
            command=widget['command'],
            fg=widget['fg'],
            font=widget['font'],
            height=widget['height'],
            highlightcolor=widget['highlightcolor'],
            image=widget['image'],
            justify=widget['justify'],
            padx=widget['padx'],
            pady=widget['pady'],
            relief=widget['relief'],
            state=widget['state'],
            text=widget['text'],
            underline=widget['underline'],
            width=widget['width'],
            wraplength=widget['wraplength']
        )
    
    button.pack()
    
def label(app, widget):
    widget = widget[1]
    
    label = TkinterLabel(
        master=app.window,
        anchor=widget['anchor'],
        bg=widget['bg'],
        bitmap=widget['bitmap'],
        bd=widget['bd'],
        cursor=widget['cursor'],
        font=widget['font'],
        fg=widget['fg'],
        height=widget['height'],
        image=widget['image'],
        justify=widget['justify'],
        padx=widget['padx'],
        pady=widget['pady'],
        relief=widget['relief'],
        text=widget['text'],
        textvariable=widget['textvariable'],
        underline=widget['underline'],
        width=widget['width'],
        wraplength=widget['wraplength']
    )
    
    label.pack()