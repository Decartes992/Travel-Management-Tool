from ast import main
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import Canvas, Button
from ttkbootstrap.scrolled import ScrolledFrame
from PIL import Image, ImageTk

class HomeScreen(tk.Frame):
    def __init__(self, master=None, show_main_view=None):
        super().__init__(master)
        self.show_main_view = show_main_view
        self.pack(fill="both", expand=True)
        
        # Create a canvas for drawing
        self.canvas = Canvas(self, bg="#000000", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        
        # Load and place the background image
        bg_image_path = "BackgroundImage.png" 
        bg_image = Image.open(bg_image_path)
        self.bg_photoimage = ImageTk.PhotoImage(bg_image)
        self.canvas.create_image(720.0, 512.0, image=self.bg_photoimage)
   


        self.canvas.create_text(
           100.0, 50.0, anchor="nw",
            text="Travel Itineraries",
            fill="#FFFFFF",
            font=("Roboto", 24)
        )


        # Add the ScrolledFrame
        self.scroll_frame = ScrolledFrame(self.canvas)
        self.scroll_frame.pack(fill="both", expand=True)
        self.scroll_frame.place(x=100, y=150, width=1240, height=800)

        # Add a widget to the ScrolledFrame
        label = tk.Label(self.scroll_frame, text="Hello, world!")
        label.pack()
        
        self.back_label = tk.Label(
            self,
            text="Back",
            bg="black",
            fg="white",
            borderwidth=0,
            highlightthickness=0
        )
        self.back_label.place(x=10.0, y=5.0, width=80, height=40.0)
        self.back_label.bind("<Button-1>", self.on_back_button_click)
      
        
    def on_back_button_click(self,  event=None):
        print("Back button was clicked")
        if self.show_main_view is not None:
            self.show_main_view()  # Show the MainView