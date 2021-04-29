from django.db import models

# Create your models here.

class doctors(models.Model):

    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    qualification = models.CharField(max_length=100)
    contact = models.CharField(max_length=13)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

