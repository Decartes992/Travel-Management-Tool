import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
from ttkbootstrap.widgets import DateEntry, Floodgauge, Meter


# window = ttk.Window(themename = 'darkly')
# window.title('extra widgets')

        # # calendar 
        # calendar = DateEntry(self)
        # calendar.pack(pady = 10)
class MainView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        title_label = tk.Label(self, text="Welcome to the Travel Itinerary Planner", font=("Arial", 16))
        title_label.pack(pady=20)

        itinerary_button = tk.Button(self, text="Manage Itineraries", command=self.open_itinerary_view)
        itinerary_button.pack(pady=10)

        activity_button = tk.Button(self, text="Manage Activities", command=self.open_activity_view)
        activity_button.pack(pady=10)



    def open_itinerary_view(self):
        self.pack_forget()  # Hide the main view
        ItineraryView(master=self.master).pack()  # Show the itinerary view

    def open_activity_view(self):
        # Placeholder function to open the activity view
        print("Activity View Opened")

class ItineraryView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Itinerary Management", font=("Arial", 16))
        self.title_label.pack(pady=20)

root = tk.Tk()
style = Style(theme='cyborg')
root.title("Travel Itinerary Planning and Management Tool")
root.geometry("600x400")

main_view = MainView(master=root)
main_view.pack()

root.mainloop()