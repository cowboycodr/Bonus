import tkinter as tk
from screeninfo import get_monitors
import time

class Window:
    def __init__(self, title='Window', size=(None, None), position=(None, None)):

        if size[0] == None or size[1] == None:
            self.size = (800, 600)
        else: 
            self.size = (size[0], size[1])

        self.width = self.size[0]
        self.height = self.size[1]

        self.window = tk.Tk()
        self.window.title(title)
        self.resize(self.width, self.height)

        if position[0] == None or position[1] == None:
            self.position = (self.window.winfo_x(), self.window.winfo_y())
            self.position_x = self.position[0]
            self.position_y = self.position[1]
        else: 
            self.position = (position[0], position[1])
            self.position_x = self.position[0]
            self.position_y = self.position[1]

        self.relocate(self.position_x, self.position_y)

        self.running = True
        self.dt = 0.0

        self.changes = {
            'width' : 0,
            'height' : 0,
            'x' : 0,
            'y' : 0,
            'dt' : self.dt
        }

        self.window.protocol('WM_DELETE_WINDOW', self.close_protocol)
        
        self.window.bind('<Configure>', self.change_protocol)
        self.window.bind('<F11>', self.fullscreen)

        self.binds = [
                {'<Configure>' : self.change_protocol},
                {'<F11>' : self.fullscreen}
            ]


    def fullscreen(self, event=None):
        if self.window.attributes('-fullscreen'):
            self.window.attributes('-fullscreen', False)
        else: 
            self.window.attributes('-fullscreen', True)

    def normal(self, event=None):
        self.window.wm_state('normal')

    def relocate(self, x, y):
        if x < 0:
            x = '-{}'.format(x)
        else:
            x = '+{}'.format(x)
        
        if y < 0:
            y = '-{}'.format(y)
        else:
            y = '+{}'.format(y)

        self.window.geometry('{}x{}{}{}'.format(self.width, self.height, x, y))

    def resize(self, width, height):
        self.window.geometry('{}x{}'.format(width, height))

        self.width = width
        self.height = height
        self.size = (self.width, self.height)

    def close_protocol(self):
        self.running = False

        self.window.destroy()
        self.on_close()

    def on_close(self, context=0):
        pass

    def on_change(self, changes):
        pass

    def change_protocol(self, configure):
        self.changes = {
            'width' : configure.width - self.width,
            'height' : configure.height - self.height,
            'x' : configure.x - self.position_x,
            'y' : configure.y - self.position_y,
            'dt' : self.dt
        }

        self.width = configure.width
        self.height = configure.height
        self.size = (self.width, self.height)

        self.position_x = configure.x
        self.position_y = configure.y
        self.position = (self.position_x, self.position_y)

        self.on_change(self.changes)

    def details(self):
        return {
            'width' : self.width,
            'height' : self.height,
            'x' : self.position_x,
            'y' : self.position_y,
            'dt' : self.dt
        }

    def center(self, resize=True, relocate=True, width=None, height=None):
        if width == None:
            width = self.window.winfo_screenwidth()
        if height == None:
            height = self.window.winfo_screenheight()
        
        if resize:
            self.resize(int(width / 2), int(height / 2))
        
        if relocate:
            self.relocate(int((width / 2) - self.width / 2), int((height / 2) - self.height / 2))

    def run(self):

        loop = 0.0
        end_loop = 0.0

        while True:
            if not self.running:
                break
            
            self.update(self.changes)
            self.window.update()
            
            loop = time.time()
            self.dt = loop - end_loop
            self.changes = {
                'width' : 0,
                'height' : 0,
                'x' : 0,
                'y' : 0,
                'dt' : self.dt
            }
            end_loop = time.time()

    def update(self, changes):
        pass