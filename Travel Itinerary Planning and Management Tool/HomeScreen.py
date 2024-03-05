import tkinter as tk
from GUI import window 
from ttkbootstrap.scrolled import ScrolledFrame



scroll_frame = ScrolledFrame(window)
scroll_frame.pack(expand = True, fill = 'both')

class HomeScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        # Add your widgets here
        