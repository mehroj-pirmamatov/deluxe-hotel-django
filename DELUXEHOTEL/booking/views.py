from django.shortcuts import render
from django.views.generic import CreateView 
from django.urls import reverse_lazy

from.models import Booking
from.forms import BookingForm


class BookingView(CreateView):
    form_class=BookingForm
    template_name="booking/booking.html"
    success_url=reverse_lazy("index")


    def get_queryset(self):
        return Booking.objects.all()
    
