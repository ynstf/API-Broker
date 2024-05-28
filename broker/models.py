from django.db import models
from django.contrib.auth.models import User


class Broker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Buyer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Salesman(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=4,decimal_places=2)
    def __str__(self):
        return self.name

class Reservation(models.Model):
    salesman = models.ForeignKey(Salesman, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    

    final_price = models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return f"broker : {self.broker} ,product : {self.product}"
    
