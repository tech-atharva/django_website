from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=35)
    phone = models.CharField(max_length=10)
    massage = models.TextField()

    def __str__(self):
        return self.email
