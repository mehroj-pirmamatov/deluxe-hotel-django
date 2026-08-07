from django.shortcuts import render
from django.views.generic import CreateView 
from django.urls import reverse_lazy

from .models import Contact
from .forms import ContactForm

class ContactView(CreateView):
    model=Contact
    form_class=ContactForm
    template_name="contact/contact.html"
    success_url=reverse_lazy("contact")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["location"] =(
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d99419.98976594552!2d65.70939651138374!3d38.85822555154009!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3f4ea63944a8e4c1%3A0x694369ac2037509d!2z0JrQsNGA0YjQuCwg0JrQsNGI0LrQsNC00LDRgNGM0Y8sINCj0LfQsdC10LrQuNGB0YLQsNC9!5e0!3m2!1sru!2s!4v1780461530806!5m2!1sru!2s" 
        )
        return context
    



