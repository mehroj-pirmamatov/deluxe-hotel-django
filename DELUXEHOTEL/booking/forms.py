from django import forms
from.models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model=Booking
        fields=("full_name","phone","email","book_time","room","status")


        widgets={
            "room":forms.Select(attrs={
                "class":"select-booking"
            }),
            "book_time":forms.TextInput(attrs={
                "type":"date"
            }),
        }