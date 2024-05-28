from django.contrib import admin
from .models import Broker, Buyer, Salesman, Product, Reservation

admin.site.register(Broker)
admin.site.register(Buyer)
admin.site.register(Salesman)
admin.site.register(Product)
admin.site.register(Reservation)