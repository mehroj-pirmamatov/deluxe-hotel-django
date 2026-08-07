from django.urls import path
from.views import ContactListView, OverView, RoomListView, BookingListView
from .views import OverView

urlpatterns = [
    path("over/view",OverView.as_view(),name="overview"),
    path("room/",RoomListView.as_view(),name="owner-room"),
    path("owner-booking/",BookingListView.as_view(),name="owner_booking"),
    path("contact/",ContactListView.as_view(),name="owner-contact"),
]

