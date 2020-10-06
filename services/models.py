from django.db import models

# Create your models here.


class Wordpress_comment(models.Model):
    email = models.EmailField(max_length=50)
    massage = models.TextField()

    def __str__(self):
        return self.email


class Html_Css_Javascript(models.Model):
    email = models.EmailField(max_length=50)
    massage = models.TextField()

    def __str__(self):
        return self.email


class PythonandDjango(models.Model):
    email = models.EmailField(max_length=50)
    massage = models.TextField()

    def __str__(self):
        return self.email
