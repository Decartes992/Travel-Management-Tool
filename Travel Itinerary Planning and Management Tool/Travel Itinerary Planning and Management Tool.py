import tkinter as tk
from tkinter import ttk

class MainView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        title_label = ttk.Label(self, text="Welcome to the Travel Itinerary Planner", font=("Arial", 16))
        title_label.pack(pady=20)

        itinerary_button = ttk.Button(self, text="Manage Itineraries", command=self.open_itinerary_view)
        itinerary_button.pack(pady=10)

        activity_button = ttk.Button(self, text="Manage Activities", command=self.open_activity_view)
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
        self.title_label = ttk.Label(self, text="Itinerary Management", font=("Arial", 16))
        self.title_label.pack(pady=20)
        back_button = ttk.Button(self, text="Back", command=self.back_to_main)
        back_button.pack(pady=10)

        itinerary_list = ttk.Treeview(self)
        itinerary_list.pack(pady=20)
        itinerary_list['columns'] = ("#1", "#2")
        itinerary_list.column("#0", width=0, stretch=tk.NO)
        itinerary_list.column("#1", anchor=tk.W, width=80)
        itinerary_list.column("#2", anchor=tk.W, width=120)
        itinerary_list.heading("#1", text="Itinerary Name", anchor=tk.W)
        itinerary_list.heading("#2", text="Destination", anchor=tk.W)

    def back_to_main(self):
        self.pack_forget()  # Hide the itinerary view
        MainView(master=self.master).pack()  # Show the main view

root = tk.Tk()
root.title("Travel Itinerary Planning and Management Tool")
root.geometry("600x400")

main_view = MainView(master=root)
main_view.pack()

root.mainloop()