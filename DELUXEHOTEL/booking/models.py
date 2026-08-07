from django.db import models
from rooms.models import Rooms

class Booking(models.Model):

    STATUS_CHOISE=(
        ("Kutilmoqda", "Kutilmoqda"),
        ("Keldi", "Keldi"),
        ("Bekor qilingan", "Bekor qilingan"),
    )


    room=models.ForeignKey(Rooms,on_delete=models.CASCADE,)
    full_name=models.CharField( max_length=100)
    phone=models.CharField( max_length=50)
    email=models.EmailField( max_length=254, null=True,blank=True)
    book_time=models.DateTimeField( auto_now_add=False)
    status=models.CharField(choices=STATUS_CHOISE,max_length=50,default="Kutilmoqda")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

