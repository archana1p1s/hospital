from django import forms
from . models import Booking


class Date(forms.DateInput):
    input_type="date"

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets={
           "booking_date":Date()
        }

        labels={
            "patient_name":"Name",
            "patient_number":"Phone Number",
            "patient_email":"Email",
            "doc_name":"Doctors",
            "booking_date":"Booking Date"
        }

