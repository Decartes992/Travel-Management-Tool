"""
File: delete_itinerary.py
Author: Iftekhar Rafi
Dal ID: B00871031

This file contains the implementation of the DeleteItinerary class, which is a tkinter-based GUI window for deleting an itinerary from a travel itinerary planning and management tool. The class provides a confirmation message asking the user if they are sure they want to delete the itinerary, and handles the deletion process accordingly.

The DeleteItinerary class inherits from the tk.Toplevel class and includes the following methods:
- __init__(self, master=None, itinerary=None): Initializes the DeleteItinerary window with the given master window and itinerary.
- on_yes_button_click(self): Handles the deletion process when the user clicks the "Yes" button.
- on_no_button_click(self): Closes the window without deleting the itinerary when the user clicks the "No" button.
"""

import tkinter as tk
import json
from tkinter import messagebox

YES_BUTTON_X = 110
NO_BUTTON_X = YES_BUTTON_X + 39
Y_OFFSET = 100

class DeleteItinerary(tk.Toplevel):
    def __init__(self, master=None, itinerary=None):
        super().__init__(master)
        self.title("Delete Itinerary")
        self.geometry("300x200")  # Set the window size to 200x100
        self.itinerary = itinerary

        # Create a label to display the confirmation message
        self.label = tk.Label(self, text="Are you sure you want\nto delete this itinerary?")
        self.label.pack()

        # Create a Yes button
        self.yes_button = tk.Button(self, text="Yes", command=self.on_yes_button_click)
        self.yes_button.place(x=YES_BUTTON_X, y=Y_OFFSET)

        # Create a No button
        self.no_button = tk.Button(self, text="No", command=self.on_no_button_click)
        self.no_button.place(x=NO_BUTTON_X, y=Y_OFFSET)
        

    def on_yes_button_click(self):
        # Load the existing itineraries from the JSON file
        try:
            with open("itinerary.json", "r") as file:
                existing_itineraries = json.load(file)
        except FileNotFoundError:
            existing_itineraries = []

        # Remove the selected itinerary from the list of existing itineraries
        existing_itineraries.remove(self.itinerary)

        # Write the updated list of itineraries to the JSON file
        with open("itinerary.json", "w") as file:
            json.dump(existing_itineraries, file, indent=4)
        
        self.master.load_itineraries()
        # Close the window
        self.destroy()

    def on_no_button_click(self):
        # Close the window without deleting the itinerary
        self.destroy()
