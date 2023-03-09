from django.db import models

# Create your models here.

class deatilescustomer(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    confirmpassword = models.CharField(max_length=100, null=True, blank=True)

class contact(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)
class savecheckoutdb(models.Model):
    FName = models.CharField(max_length=100, null=True, blank=True)
    SName = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    Pincode = models.EmailField(max_length=100, null=True, blank=True)
