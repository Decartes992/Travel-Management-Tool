
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
from ttkbootstrap.widgets import DateEntry, Floodgauge, Meter

class CreateItineraryView(tk.Frame):
     def __init__(self, master=None):
         super().__init__(master)
         self.pack()
        
         self.title_label = tk.Label(self, text="Create Itinerary", font=("Arial", 16))
         self.title_label.pack(pady=20)

         self.destination_label = tk.Label(self, text="Destination:")
         self.destination_label.pack(pady=10)
         self.destination_entry = tk.Entry(self)
         self.destination_entry.pack(pady=10)

         self.start_date_label = tk.Label(self, text="Start Date:")
         self.start_date_label.pack(pady=10)
         self.start_date_entry = DateEntry(self)
         self.start_date_entry.pack(pady=10)

         self.end_date_label = tk.Label(self, text="End Date:")
         self.end_date_label.pack(pady=10)
         self.end_date_entry = DateEntry(self)
         self.end_date_entry.pack(pady=10)

         self.create_button = tk.Button(self, text="Create Itinerary", command=self.create_itinerary)
         self.create_button.pack(pady=20)