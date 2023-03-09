from django.db import models

# Create your models here.
class admindb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Email=models.EmailField(max_length=30,null=True,blank=True)
    Password=models.CharField(max_length=30,null=True,blank=True)
    Confirmpassword=models.CharField(max_length=30,null=True,blank=True)
    Image=models.ImageField(max_length=30,null=True,blank=True)
class categorydb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Discription=models.CharField(max_length=30,null=True,blank=True)
    Image=models.ImageField(upload_to="media", null=True,blank=True)
class productdb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    CATEGORY = models.CharField(max_length=100, null=True, blank=True)
    Price=models.CharField(max_length=30,null=True,blank=True)
    Discription=models.CharField(max_length=30,null=True,blank=True)
    Quantity=models.CharField(max_length=30,null=True,blank=True)
    Image=models.ImageField(max_length=30,null=True,blank=True)
    Image2 = models.ImageField(max_length=30, null=True, blank=True)
    Image3 = models.ImageField(max_length=30, null=True, blank=True)

class cartdb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Total=models.IntegerField(null=True,blank=True)

