from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Broker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)

    def saveing_rate(self):
        all_reservation = Reservation.objects.filter(broker=self)
        save = 0
        for reservation in all_reservation:
            save += reservation.saveing()
        return round(save/len(all_reservation),2)
    
    def __str__(self):
        return self.name

class Buyer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Salesman(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    owner = models.ForeignKey(Salesman, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    def __str__(self):
        return self.name

class Reservation(models.Model):
    salesman = models.ForeignKey(Salesman, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    final_price = models.IntegerField()

    def  saveing(self):
        save = round( (1-(self.final_price/self.product.price))*100 ,2)
        return save

    def __str__(self):
        return f"broker : {self.broker} ,product : {self.product}"
    
