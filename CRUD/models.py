from django.db import models

class Employees(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=300,null=True,blank=True)  # Add address column
    phone_number = models.CharField(max_length=20,null=True,blank=True)  # Add phone number field

    def __str__(self):
        return self.name
