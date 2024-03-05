import datetime
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
from ttkbootstrap.widgets import DateEntry, Floodgauge, Meter
from create_itinerary_view import CreateItineraryView
from ViewItinerariesView import ItineraryView
import os
from tkinter import PhotoImage, Canvas, Button
from pathlib import Path

# Change the current working directory to the directory of this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Define a function to get the path to an asset
def relative_to_assets(path: str) -> Path:
    return Path("./assets") / Path(path)

class MainView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        # Set the background color of the frame
        self.configure(bg = "#000000")

        # Create a canvas for drawing
        self.canvas = Canvas(
            self,
            bg = "#000000",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        # Place the canvas in the frame
        self.canvas.place(x = 0, y = 0)

        # Load an image and create an image object on the canvas
        image_image_1 = PhotoImage(file=relative_to_assets("BackgroundImage.png"))
        self.image_1 = self.canvas.create_image(720.0, 512.0, image=image_image_1)

        # Load an image for the button and create a button object on the canvas
        button_image_1 = PhotoImage(file=relative_to_assets("StartButton.png"))
        self.button_1 = Button(
            self,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(x=580.0, y=480.0, width=280.0, height=64.0)

        # Create text objects on the canvas
        self.canvas.create_text(
            500.0,
            365.0,
            anchor="nw",
            text="Easily Create and Manage Itineraries",
            fill="#FFFBFB",
            font=("RobotoRoman Regular", 24 * -1)
        )

        self.canvas.create_text(
            453.0,
            263.0,
            anchor="nw",
            text="Travel Tool",
            fill="#FFFFFF",
            font=("RobotoRoman Medium", 96 * -1)
        )

root = tk.Tk()
style = Style(theme='cyborg')
root.title("Travel Itinerary Planning and Management Tool")

# Create an instance of MainView and pack it into the root window
main_view = MainView(root)
main_view.pack()

root.resizable(False, False)
root.mainloop()