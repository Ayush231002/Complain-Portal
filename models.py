from django.db import models

# Create your models here.
class sign(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    contact = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    


        