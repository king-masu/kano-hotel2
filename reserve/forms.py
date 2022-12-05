from datetime import date
from django.forms import Form, ModelForm, DateField, widgets
from django import forms
from .models import Reservation

today = date.today()

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('customer_name', 'customer_email', 'customer_number', 'date_from', 'date_to', 'days')
        # date_from = forms.DateField(widget=forms.DateInput(attrs={'min': today, 'value': today, 'type': 'date'}), required=True)

        widgets = {
            'date_from': widgets.DateInput(attrs={'type': 'date', 'value': today}),
            'date_to': widgets.DateInput(attrs={'type': 'date'}),
        }