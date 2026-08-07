from django.db import models

class RoomType(models.Model):
    room_type=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.room_type
    

class Rooms(models.Model):

    STATUS_CHOISE=(
        ("Avaible", "Avaible"),
        ("Booked", "Booked"),
        ("Cleaning", "Cleaning"),
        ("Closed", "Closed"),
    )

    room_name=models.CharField(max_length=50)
    room_number=models.PositiveIntegerField()
    room_type=models.ForeignKey(RoomType, on_delete=models.CASCADE)
    people=models.PositiveIntegerField(default=1)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    size=models.PositiveIntegerField()
    view=models.CharField(max_length=50)
    bed=models.PositiveIntegerField()
    status=models.CharField(choices=STATUS_CHOISE,max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.room_type)

    