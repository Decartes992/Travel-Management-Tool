import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
from ttkbootstrap.widgets import DateEntry, Floodgauge, Meter


class ItineraryView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Itinerary Management", font=("Arial", 16))
        self.title_label.pack(pady=20)