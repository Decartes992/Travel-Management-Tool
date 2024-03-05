import json
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import Canvas, Button, Entry
from ttkbootstrap.scrolled import ScrolledFrame
from PIL import Image, ImageTk
from Add_itinerary import AddItinerary
from models import Itinerary, Destination, Hotel
from edit_itinerary import EditItinerary
from delete_itinerary import DeleteItinerary


IB_Y_OFFSET = 863.34 # Y offset for the itinerary buttons
IB_WIDTH = 225.0 # Width of the itinerary buttons
IB_HEIGHT = 65.0 # Height of the itinerary buttons
X_GENERAL_OFFSET = 180 # X offset for the general activities
SCROLLED_FRAME_WITDTH = 1080 # Width of the scrolled frame
SCROLLED_FRAME_HEIGHT = 682.67 # Height of the scrolled frame
SCROLLED_FRAME_Y_OFFSET = 170.67 # Y offset for the scrolled frame

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
   
        # Add a label for the title
        self.canvas.create_text(
           X_GENERAL_OFFSET, 110.0, anchor="nw",
            text="Travel Itineraries",
            fill="#FFFFFF",
            font=("Roboto", 24)
        )

        # Add the ScrolledFrame
        self.scroll_frame = ScrolledFrame(self.canvas)
        self.scroll_frame.pack(fill="both", expand=True)
        self.scroll_frame.place(x=X_GENERAL_OFFSET, y=SCROLLED_FRAME_Y_OFFSET, width=SCROLLED_FRAME_WITDTH, height=SCROLLED_FRAME_HEIGHT)
 


        # Add a label for the back button
        self.back_label = tk.Label(
            self,
            text="Back",
            bg="black",
            fg="white",
            borderwidth=0,
            highlightthickness=0
        )
        self.back_label.place(x=10.0, y=5.0, width=80, height=40.0)
        self.back_label.bind("<Button-1>",lambda event: show_main_view() )
        
        # Add a label for the Add Itinerary button
        self.add_label = tk.Label(
            self,
            text="Add Itinerary",
            bg="black",
            fg="white",
            borderwidth=0,
            highlightthickness=0
        )
        self.add_label.place(x=X_GENERAL_OFFSET, y=IB_Y_OFFSET, width=IB_WIDTH, height=IB_HEIGHT)
        self.add_label.bind("<Button-1>",lambda event: AddItinerary())
        
        # Add a label for the Refresh button
        self.add_label = tk.Label(
            self,
            text="Refresh List",
            bg="black",
            fg="white",
            borderwidth=0,
            highlightthickness=0
        )
        self.add_label.place(x= X_GENERAL_OFFSET + SCROLLED_FRAME_WITDTH - IB_WIDTH, y=IB_Y_OFFSET, width=IB_WIDTH, height=IB_HEIGHT)
        self.add_label.bind("<Button-1>",lambda event: self.load_itineraries())


        # Create a list to store itinerary labels
        self.itinerary_labels = []
        
        # Call a method to populate the itineraries
        self.load_itineraries()
        
        self.search_label = tk.Label(
            self,
            text="Search Country",
            bg="black",
            fg="white",
            borderwidth=0,
            highlightthickness=0
        )
        self.search_label.place(x= X_GENERAL_OFFSET + SCROLLED_FRAME_WITDTH - IB_WIDTH, y=100, width=IB_WIDTH, height=IB_HEIGHT)
        self.search_label.bind("<Button-1>", self.on_search_entry_return)

        self.search_entry = Entry(self)
        
        self.search_entry.place(x=X_GENERAL_OFFSET + SCROLLED_FRAME_WITDTH/2 - 2*IB_WIDTH/3, y=125, width=IB_WIDTH*2, height=30)
        self.search_entry.bind("<Return>", self.on_search_entry_return)

        
    def on_search_entry_return(self, event):
        search_text = self.search_entry.get().lower()
        self.load_itineraries(search_text)

    # Modify the load_itineraries method in the HomeScreen class
    def load_itineraries(self, search_text=""):
        # Clear existing itinerary labels
        for label in self.itinerary_labels:
            label.destroy()

        # Load the existing itineraries from the JSON file
        try:
            with open("itinerary.json", "r") as file:
                existing_itineraries = json.load(file)
        except FileNotFoundError:
            existing_itineraries = []

        # Clear the scrolled frame
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        # Add the headers
        self.scrollable_window_heading()

        # Add a label and a button for each itinerary using grid
        for i, itinerary in enumerate(existing_itineraries):
            if search_text in itinerary["Country"].lower():
                self.create_itinerary_frame(itinerary, i + 1)  # Plus 1 to account for the header row



        def load_itineraries(self):
            # Clear existing itinerary labels
            for label in self.itinerary_labels:
                label.destroy()

            # Load the existing itineraries from the JSON file
            try:
                with open("itinerary.json", "r") as file:
                    existing_itineraries = json.load(file)
            except FileNotFoundError:
                existing_itineraries = []

            # Clear the scrolled frame
            for widget in self.scroll_frame.winfo_children():
                widget.destroy()

            # Add the headers
            self.scrollable_window_heading()

            # Add a label and a button for each itinerary using grid
            for i, itinerary in enumerate(existing_itineraries):
                self.create_itinerary_frame(itinerary, i + 1)  # Plus 1 to account for the header row

    def create_itinerary_frame(self, itinerary, row):
        # Create a new frame for each itinerary
        frame = tk.Frame(self.scroll_frame)
        frame.grid(row=row, column=0, sticky='ew', padx=10, pady=2)
        self.scroll_frame.grid_columnconfigure(0, weight=1)

        # Define the column widths (adjust the width as needed)
        column_widths = [10, 10, 13, 18, 30, 8, 8]

        # Create labels with a fixed width and buttons using grid within the frame
        tk.Label(frame, text=itinerary["Departure Date"], width=column_widths[0]).grid(row=0, column=0)
        tk.Label(frame, text=itinerary["Return Date"], width=column_widths[1]).grid(row=0, column=1)
        tk.Label(frame, text=itinerary["City"], width=column_widths[2]).grid(row=0, column=2)
        tk.Label(frame, text=itinerary["Country"], width=column_widths[3]).grid(row=0, column=3)
        tk.Label(frame, text=itinerary["Hotel Name"], width=column_widths[4]).grid(row=0, column=4)
        ttk.Button(frame, bootstyle='darkly', text='Edit', width=column_widths[5], command=lambda: EditItinerary(master=self, itinerary=itinerary)).grid(row=0, column=5)
        ttk.Button(frame, bootstyle='danger', text='Delete', width=column_widths[6], command=lambda: DeleteItinerary(master=self, itinerary=itinerary)).grid(row=0, column=6)

        # Set the column weights to control the expansion of each column
        for index, width in enumerate(column_widths):
            frame.grid_columnconfigure(index, weight=width)

    def scrollable_window_heading(self):
        # Add the header labels to the first row of the grid
        header_frame = tk.Frame(self.scroll_frame)
        header_frame.grid(row=0, column=0, sticky='ew')
        self.scroll_frame.grid_columnconfigure(0, weight=1)

        # Define the column widths (adjust the width as needed)
        column_widths = [12, 8, 15, 17, 30]

        headers = ["Departure", "Return", "City", "Country", "Hotel Name"]
        for index, text in enumerate(headers):
            label = tk.Label(header_frame, text=text, width=column_widths[index])
            label.grid(row=0, column=index)
            