import datetime


class TravelItinerary:
    def __init__(self, destination, start_date, end_date):
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.activities = []

    def add_activity(self, activity):
        self.activities.append(activity)

    def remove_activity(self, activity):
        self.activities.remove(activity)

    def get_activities(self):
        return self.activities

    def get_duration(self):
        return (self.end_date - self.start_date).days

# Example usage
destination = "Paris"
start_date = datetime.date(2022, 9, 1)
end_date = datetime.date(2022, 9, 7)

itinerary = TravelItinerary(destination, start_date, end_date)

itinerary.add_activity("Visit Eiffel Tower")
itinerary.add_activity("Explore Louvre Museum")
itinerary.add_activity("Take a boat tour on the Seine River")

activities = itinerary.get_activities()
for activity in activities:
    print(activity)

duration = itinerary.get_duration()
print(f"Duration of the trip: {duration} days")