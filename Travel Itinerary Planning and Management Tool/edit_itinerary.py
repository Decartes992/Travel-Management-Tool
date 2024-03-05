"""
File: edit_itinerary.py
Author: Iftekhar Rafi
Dal ID: B00871031

This file contains the implementation of the EditItinerary class, which is a tkinter-based GUI window for editing travel itineraries. It allows the user to modify the details of a specific itinerary, such as the city, country, departure date, return date, hotel name, and hotel address. The edited itinerary is then saved to a JSON file.

The EditItinerary class inherits from the tk.Toplevel class and provides a user-friendly interface for updating itinerary details. It includes labels and entry fields for each detail, as well as a submit button to save the changes. The class also utilizes the pycountry library to retrieve a list of countries for the country field and the ttkbootstrap library for styling the GUI components.

The class methods handle the retrieval of countries, the submission of the updated itinerary, and the updating of the JSON file containing the itineraries. The updated itinerary is printed to the console for verification.


"""
import tkinter as tk
import json
from tkinter import ttk
from models import Itinerary, Destination, Hotel
import pycountry
from ttkbootstrap.widgets import DateEntry
from ttkbootstrap import Style

class EditItinerary(tk.Toplevel):
    def __init__(self, master=None, itinerary=None):
        super().__init__(master)
        self.title("Edit Itinerary")
        self.geometry("400x500")  # Set the window size to 500x400
        self.itinerary = itinerary

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

        # Populate the entries with the current itinerary details
        if itinerary is not None:
            for label in self.labels:
                if label in ["Departure Date", "Return Date"]:
                    self.entries[label].entry.delete(0, 'end')  # Clear the entry field
                    self.entries[label].entry.insert(0, itinerary[label])
                else:
                    self.entries[label].delete(0, 'end')  # Clear the entry field
                    self.entries[label].insert(0, itinerary[label])


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

        # Replace the existing itinerary with the updated one
        for i, existing_itinerary in enumerate(existing_itineraries):
            if existing_itinerary == self.itinerary:
                existing_itineraries[i] = itinerary_dict
                break

        # Write the updated list of itineraries to the JSON file
        with open("itinerary.json", "w") as file:
            json.dump(existing_itineraries, file, indent=4)
            
        self.master.load_itineraries()
        # Close the window
        self.destroy()
