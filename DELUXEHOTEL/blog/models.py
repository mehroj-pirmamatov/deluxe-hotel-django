from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=500)
    image=models.ImageField(upload_to="blog/image/", max_length=100)
    created_at=models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name="bloglar"
        verbose_name_plural="ModelNames"