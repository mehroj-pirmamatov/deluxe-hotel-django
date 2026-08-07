from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from contact.models import Contact
from rooms.models import Rooms, RoomType
from contact.models import Contact 
from booking.models import Booking
from .forms import RoomForm  
from booking.forms import BookingForm                                                           

class OverView(ListView):
    login_url="/login"
    redirect_field_name="login"
    template_name="owner/owner-dashboard.html"

    def get_queryset(self):
        return Contact.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] = Rooms.objects.filter(status="Avaible").count()
        context["bookings_count"] = Booking.objects.count()
        context["contacts"] = Contact.objects.all().count()
        context["contact_infos"] = Contact.objects.all().order_by("-created_at")

        return context
    

class RoomListView(
    LoginRequiredMixin,
    ListView,
    FormView,
):
    login_url="/login"
    redirect_field_name="login"
    
    template_name="owner/owner-rooms.html"
    form_class=RoomForm
    success_url=reverse_lazy("owner-room")

    def get_queryset(self):
        return Rooms.objects.all()
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] =Rooms.objects.all().order_by("created_at")
        context["room_types"] = RoomType.objects.all()
        return context
    
    
    
    
class BookingListView(LoginRequiredMixin,ListView,FormView):
    login_url="/login"
    redirect_field_name="login"
    template_name= "owner/owner-bookings.html"
    form_class=BookingForm
    success_url=reverse_lazy("owner_booking")

    def get_queryset(self):
        return Booking.objects.all()
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["bookings"]=Booking.objects.all().order_by("-created_at")
        context["today_count"]=Booking.objects.filter(created_at__date=timezone.now().date()).count()
        context["pending_count"]=Booking.objects.filter(status="Kutilmoqda").count()
        context["confirmed_count"]=Booking.objects.filter(status="Keldi").count()
        context["cancelled_count"]=Booking.objects.filter(status="Bekor qilingan").count()
        return context

   
    
    

class ContactListView(LoginRequiredMixin,ListView):
    login_url="/login"
    redirect_field_name="login"
    template_name= "owner/owner-messages.html"

    def get_queryset(self):
        return Contact.objects.all()
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["contacts"]=Contact.objects.all().order_by("-created_at")
        return context
    
