from django.db import models

class Contact(models.Model):
    full_name=models.CharField( max_length=100)
    email=models.EmailField( max_length=254)
    phone=models.CharField( max_length=50)
    subject=models.CharField(max_length=50)
    description=models.TextField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
