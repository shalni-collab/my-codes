from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import User

class User(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    mobile_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name
    
    # admin/ director models are here

class Director(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=25)


    def __str__(self):
        return self.email

