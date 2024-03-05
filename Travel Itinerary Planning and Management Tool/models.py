"""
File: models.py
Author: Iftekhar Rafi
Dal ID: B00871031

This file contains the implementation of the classes used in the Travel Itinerary Planning and Management Tool.

Classes:
- Destination: Represents the travel destination with city and country.
- Hotel: Stores details of the hotel for the trip.
- Itinerary: Stores and manages details of a travel itinerary.
"""

class Destination:
    """Represents the travel destination with city and country."""
    def __init__(self, city, country):
        self.city = city
        self.country = country

    def __str__(self):
        return f"Destination: {self.city}, {self.country}"


class Hotel:
    """Stores details of the hotel for the trip."""
    def __init__(self, name = "None", address = "None"):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Hotel: {self.name}, Address: {self.address}"


class Itinerary:
    """Stores and manages details of a travel itinerary."""
    def __init__(self, destination, departure_date, return_date, hotel):
        self.destination = destination
        self.departure_date = departure_date
        self.return_date = return_date
        self.hotel = hotel

    def get_summary(self):
        return {
            "destination": str(self.destination),
            "departure_date": self.departure_date,
            "return_date": self.return_date,
            "hotel": str(self.hotel),
        }

    def __str__(self):
        itinerary_summary = self.get_summary()
        return f"Itinerary for {itinerary_summary['destination']} from {itinerary_summary['departure_date']} to {itinerary_summary['return_date']}"
