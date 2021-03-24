from django.db import models

# Create your models here.
class BasicDetails(models.Model):
    name = models.CharField(max_length = 50)
    sex = models.CharField(max_length = 1)
    annual_income = models.IntegerField()
    email = models.EmailField(max_length=255)
    mobile = models.IntegerField()
    occupation = models.CharField(max_length = 50)
    DOB = models.DateField()
    user_name = models.CharField(max_length = 150)
    aadhar=models.IntegerField()
    image=models.ImageField(upload_to ='uploads/Photo')

class PresentLocation(models.Model):
    country = models.CharField(max_length = 50, default = "India")
    state = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    street = models.CharField(max_length = 50)
    pincode = models.IntegerField()
    user_name = models.CharField(max_length = 150)

class Status (models.Model):
    account_number = models.IntegerField()
    balance = models.IntegerField()
    user_name = models.CharField(max_length = 150)

class Email(models.Model):
    To=models.CharField(max_length = 150)
    subject=models.CharField(max_length=200)


