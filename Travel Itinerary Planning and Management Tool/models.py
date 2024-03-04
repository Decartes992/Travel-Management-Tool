
class Destination:
    """Represents the travel destination with city and country."""
    def __init__(self, city, country):
        self.city = city
        self.country = country

    def __str__(self):
        return f"Destination: {self.city}, {self.country}"


class Hotel:
    """Stores details of the hotel for the trip."""
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Hotel: {self.name}, Address: {self.address}"


class Activity:
    """Represents an activity with details."""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Activity: {self.name}, Description: {self.description}"


class Day:
    """Represents a specific day and the activities planned for that day."""
    def __init__(self, date):
        self.date = date
        self.activities = []

    def add_activity(self, activity):
        self.activities.append(activity)

    def remove_activity(self, activity_name):
        self.activities = [act for act in self.activities if act.name != activity_name]

    def __str__(self):
        activities_str = ', '.join([str(activity) for activity in self.activities])
        return f"Date: {self.date}, Activities: {activities_str}"


class Itinerary:
    """Stores and manages details of a travel itinerary."""
    def __init__(self, destination, departure_date, return_date, hotel):
        self.destination = destination
        self.departure_date = departure_date
        self.return_date = return_date
        self.hotel = hotel
        self.general_activities = []
        self.list_of_days = []

    def add_general_activity(self, activity):
        self.general_activities.append(activity)

    def add_day(self, day):
        self.list_of_days.append(day)

    def get_summary(self):
        return {
            "destination": str(self.destination),
            "departure_date": self.departure_date,
            "return_date": self.return_date,
            "hotel": str(self.hotel),
            "general_activities": [str(activity) for activity in self.general_activities],
            "list_of_days": [str(day) for day in self.list_of_days]
        }

    def __str__(self):
        itinerary_summary = self.get_summary()
        return f"Itinerary for {itinerary_summary['destination']} from {itinerary_summary['departure_date']} to {itinerary_summary['return_date']}"
