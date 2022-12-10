from django.db import models

# Create your models here.
class Contacts(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Email = models.EmailField()
    PhoneNumber = models.CharField(max_length=10)