import tkinter as tk
from tkinter import Canvas, Button
from HomeScreen import HomeScreen
from PIL import Image, ImageTk
import ttkbootstrap as ttk
import os

# Change the current working directory to the directory of this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MainView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        # Create a canvas for drawing
        self.canvas = Canvas(self, bg="#000000", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # Load and place the background image
        bg_image_path = "BackgroundImage.png" 
        bg_image = Image.open(bg_image_path)
        self.bg_photoimage = ImageTk.PhotoImage(bg_image)
        self.canvas.create_image(720.0, 512.0, image=self.bg_photoimage)

        # Load and place the start button image with transparency
        start_button_path = "StartButton.png" 
        start_button_image = Image.open(start_button_path)
        self.start_button_photoimage = ImageTk.PhotoImage(start_button_image)
        self.start_button = Button(
            self,
            image=self.start_button_photoimage,
            borderwidth=0,
            highlightthickness=0,
            command=self.on_start_button_click,
            relief="flat",

        )
        self.start_button.place(x=580.0, y=480.0, width=225.0, height=65.0)

        # Add text to the canvas
        self.canvas.create_text(
            450.0, 365.0, anchor="nw",
            text="Easily Create and Manage Itineraries",
            fill="#FFFBFB",
            font=("Roboto", 16)
        )
        self.canvas.create_text(
            470.0, 263.0, anchor="nw",
            text="Travel Tool",
            fill="#FFFFFF",
            font=("Roboto", 48)
        )

    def on_start_button_click(self):
        print("Start button was clicked")
        self.pack_forget()  # Hide the MainView

        self.home_screen = HomeScreen(self.master, self.show_main_view)
        self.home_screen.pack()  # Show the HomeScreen

    def show_main_view(self):
        if self.home_screen is not None:
            self.home_screen.pack_forget()  # Hide the HomeScreen
        self.pack(fill="both", expand=True)  # Show the MainView


# Main application window setup
root = ttk.Window(themename = 'darkly')
root.geometry("1440x1024")
root.title("Travel Itinerary Planning and Management Tool")

# Create an instance of MainView and pack it into the root window
main_view = MainView(root)
main_view.pack()

root.resizable(False, False)
root.mainloop()
