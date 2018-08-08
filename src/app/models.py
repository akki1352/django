from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=30)
    price = models.FloatField()
    Quantity = models.IntegerField(default=1)
    
class Register(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=80,unique=True)
    password = models.CharField(max_length=15)
    phone = models.CharField(max_length=20)

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=80)
    bookId = models.CharField(max_length=100)
    bookName = models.CharField(max_length=50)
    product = models.CharField(max_length=30)
    price = models.FloatField()
    Quantity = models.IntegerField(default=1)

class NCart(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=80)
    bookId = models.CharField(max_length=100)
    bookName = models.CharField(max_length=50)
    product = models.CharField(max_length=30)
    price = models.FloatField()
    Quantity = models.IntegerField(default=1)


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=80)
    bookId = models.CharField(max_length=100,unique=True)
    bookName = models.CharField(max_length=50,unique=True)
    product = models.CharField(max_length=30)
    price = models.FloatField()
    Quantity = models.IntegerField(default=1)
