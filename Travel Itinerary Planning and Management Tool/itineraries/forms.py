from django import forms
from .models import Itinerary

class ItineraryForm(forms.ModelForm):
    class Meta:
        model = Itinerary
        fields = ['destination', 'start_date', 'end_date', 'notes']
