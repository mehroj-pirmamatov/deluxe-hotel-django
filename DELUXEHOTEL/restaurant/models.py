from django.db import models

class Menu(models.Model):
    image=models.ImageField(upload_to="menu/image")
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=255)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

