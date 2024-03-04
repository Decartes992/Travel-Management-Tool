# To implement the flowchart for creating and managing itineraries, the following code outlines the core functionality.
# This includes the Tkinter GUI setup, asking for new itinerary details, validating input, and storing the itinerary.
# We assume that the itinerary details are stored in an XML file for simplicity.

import tkinter as tk
from tkinter import messagebox
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Function to check for data errors in user input
def validate_itinerary(title, start_date, end_date):
    errors = []
    if not title:
        errors.append("Title is required.")
    if not start_date:
        errors.append("Start date is required.")
    if not end_date:
        errors.append("End date is required.")
    return errors

# Function to store itinerary in an XML file
def store_itinerary(title, start_date, end_date):
    # Create an element tree and add itinerary details
    itinerary = ET.Element("itinerary")
    ET.SubElement(itinerary, "title").text = title
    ET.SubElement(itinerary, "start_date").text = start_date
    ET.SubElement(itinerary, "end_date").text = end_date
    
    # Append to the root element if file exists, else create new root
    try:
        tree = ET.parse('itineraries.xml')
        root = tree.getroot()
    except (ET.ParseError, FileNotFoundError):
        root = ET.Element("itineraries")
    
    root.append(itinerary)
    
    # Write the XML file with pretty printing
    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
    with open("itineraries.xml", "w") as f:
        f.write(xmlstr)

# Function to create a new itinerary
def create_new_itinerary():
    def submit_itinerary():
        title = title_entry.get()
        start_date = start_date_entry.get()
        end_date = end_date_entry.get()
        
        # Check for errors
        errors = validate_itinerary(title, start_date, end_date)
        if errors:
            messagebox.showerror("Error", "\n".join(errors))
            title_entry.delete(0, tk.END)
            start_date_entry.delete(0, tk.END)
            end_date_entry.delete(0, tk.END)
        else:
            store_itinerary(title, start_date, end_date)
            messagebox.showinfo("Success", "Itinerary successfully added.")
            new_itinerary_window.destroy()
    
    # Set up the new itinerary window
    new_itinerary_window = tk.Toplevel(root)
    new_itinerary_window.title("Create New Itinerary")
    
    tk.Label(new_itinerary_window, text="Title").pack()
    title_entry = tk.Entry(new_itinerary_window)
    title_entry.pack()
    
    tk.Label(new_itinerary_window, text="Start Date (YYYY-MM-DD)").pack()
    start_date_entry = tk.Entry(new_itinerary_window)
    start_date_entry.pack()
    
    tk.Label(new_itinerary_window, text="End Date (YYYY-MM-DD)").pack()
    end_date_entry = tk.Entry(new_itinerary_window)
    end_date_entry.pack()
    
    submit_button = tk.Button(new_itinerary_window, text="Submit", command=submit_itinerary)
    submit_button.pack()

# Main application setup
root = tk.Tk()
root.title("Travel Itinerary Planning and Management Tool")

main_menu = tk.Menu(root)
root.config(menu=main_menu)

# Add menu items
file_menu = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Itinerary", command=create_new_itinerary)
file_menu.add_command(label="Exit", command=root.quit)

# Run the main loop
root.mainloop()
