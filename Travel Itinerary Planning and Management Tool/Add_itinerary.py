"""
File: Add_itinerary.py
Author: Iftekhar Rafi
Dal ID: B00871031

This file contains the implementation of the AddItinerary class, which is a tkinter Toplevel window for adding a new itinerary to the travel itinerary planning and management tool. It provides a user interface for entering the details of the itinerary, such as city, country, departure date, return date, hotel name, and hotel address. The entered details are then used to create a Destination object, a Hotel object, and an Itinerary object. The itinerary details are printed, converted to a dictionary, and added to the list of existing itineraries stored in a JSON file. The window is closed after the submission of the itinerary.

The AddItinerary class inherits from the tkinter Toplevel class and utilizes various tkinter widgets and modules, such as ttk, pycountry, and DateEntry from ttkbootstrap. It also imports the models module, which contains the definitions of the Itinerary, Destination, and Hotel classes.

The file also includes the get_countries method, which retrieves the list of countries from a data source using the pycountry module.

"""
import tkinter as tk
import json
from tkinter import ttk
from models import Itinerary, Destination, Hotel
import pycountry

from ttkbootstrap.widgets import DateEntry
from ttkbootstrap import Style

class AddItinerary(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Add Itinerary")
        self.geometry("400x500")  # Set the window size to 500x400

        # Create labels and entries for the itinerary details
        self.labels = ["City", "Country", "Departure Date", "Return Date", "Hotel Name", "Hotel Address"]
        self.entries = {}
        for label in self.labels:
            tk.Label(self, text=label).pack()
            if label == "Country":
                self.entries[label] = ttk.Combobox(self, values=self.get_countries())
            elif label in ["Departure Date", "Return Date"]:
                self.entries[label] = DateEntry(self)
            else:
                self.entries[label] = tk.Entry(self)
            self.entries[label].pack()

        # Create a button to submit the itinerary
        self.submit_button = tk.Button(self, text="Submit", command=self.on_submit_button_click)
        self.submit_button.pack()

    def get_countries(self):
        # Retrieve the list of countries from a data source
        countries = [country.name for country in pycountry.countries]
        return countries

    def on_submit_button_click(self):
        # Get the itinerary details from the entries
        city = self.entries["City"].get()
        country = self.entries["Country"].get()
        departure_date = self.entries["Departure Date"].entry.get()
        return_date = self.entries["Return Date"].entry.get()
        hotel_name = self.entries["Hotel Name"].get()
        hotel_address = self.entries["Hotel Address"].get()

        # Create a Destination object
        destination = Destination(city, country)

        # Create a Hotel object
        hotel = Hotel(hotel_name, hotel_address)

        # Create an Itinerary object
        itinerary = Itinerary(destination, departure_date, return_date, hotel)

        # Print the itinerary details
        print(itinerary)

        # Convert the itinerary details to a dictionary
        itinerary_dict = {
            "Departure Date": departure_date,
            "Return Date": return_date,
            "City": city,
            "Country": country,
            "Hotel Name": hotel_name,
            "Hotel Address": hotel_address
        }

        # Load the existing itineraries from the JSON file
        try:
            with open("itinerary.json", "r") as file:
                existing_itineraries = json.load(file)
        except FileNotFoundError:
            existing_itineraries = []

        # Add the new itinerary to the list of existing itineraries
        existing_itineraries.append(itinerary_dict)

        # Write the updated list of itineraries to the JSON file
        with open("itinerary.json", "w") as file:
            json.dump(existing_itineraries, file, indent=4)

        self.master.load_itineraries()

        # Close the window
        self.destroy()