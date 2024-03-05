"""
Travel Itinerary Planning and Management Tool

This file contains the GUI implementation for the travel itinerary planning and management tool. It provides a graphical user interface for users to easily create and manage itineraries.

Author: Iftekhar Rafi
Dal ID: B00871031
"""

import tkinter as tk
from tkinter import Canvas, Button
from HomeScreen import HomeScreen
from PIL import Image, ImageTk
import ttkbootstrap as ttk
import os

# Change the current working directory to the directory of this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

WINDOW_HEIGHT = 1024
WINDOW_WIDTH = 1440
DEFAULT_BG = "#000000"
START_BUTTON_X = 580.0
START_BUTTON_Y = 480.0
START_BUTTON_WIDTH = 225.0
START_BUTTON_HEIGHT = 65.0


class MainView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        # Create a canvas for drawing
        self.canvas = Canvas(self, bg=DEFAULT_BG, height=WINDOW_HEIGHT, width=WINDOW_WIDTH, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # Load and place the background image
        bg_image_path = "BackgroundImage.png" 
        bg_image = Image.open(bg_image_path)
        self.bg_photoimage = ImageTk.PhotoImage(bg_image)
        self.canvas.create_image(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, image=self.bg_photoimage)

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
        self.start_button.place(x=START_BUTTON_X, y=START_BUTTON_Y, width=START_BUTTON_WIDTH, height=START_BUTTON_HEIGHT)
        

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
