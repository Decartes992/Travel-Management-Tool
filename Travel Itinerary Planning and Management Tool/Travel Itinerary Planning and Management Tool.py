import tkinter as tk
from tkinter import ttk

def open_itinerary_view():
    # Placeholder function to open the itinerary view
    print("Itinerary View Opened")

def open_activity_view():
    # Placeholder function to open the activity view
    print("Activity View Opened")

# Create the main window
root = tk.Tk()
root.title("Travel Itinerary Planning and Management Tool")

# Set the window size
root.geometry("600x400")

# Create a label for the title
title_label = ttk.Label(root, text="Welcome to the Travel Itinerary Planner", font=("Arial", 16))
title_label.pack(pady=20)

# Create buttons for navigating to different parts of the application
itinerary_button = ttk.Button(root, text="Manage Itineraries", command=open_itinerary_view)
itinerary_button.pack(pady=10)

activity_button = ttk.Button(root, text="Manage Activities", command=open_activity_view)
activity_button.pack(pady=10)

# Start the application
root.mainloop()
