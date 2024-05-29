from django.contrib import admin
from .models import Broker, Buyer, Salesman, Product, Reservation, City


class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    list_display = ["id","salesman","buyer","broker","product","final_price","saveing"]
    list_filter = ["id","salesman","buyer","broker","product","final_price"]
    list_editable = ["salesman","buyer","broker","product","final_price"]
admin.site.register(Reservation, ReservationAdmin)

class BrokerAdmin(admin.ModelAdmin):
    model = Broker
    list_display = ["id","user","name","address","saveing_rate"]
admin.site.register(Broker, BrokerAdmin)

class BuyerAdmin(admin.ModelAdmin):
    model = Buyer
    list_display = ["id","user","name","address"]
admin.site.register(Buyer, BuyerAdmin)

class SalesmanAdmin(admin.ModelAdmin):
    model = Salesman
    list_display = ["id","user","name","address"]
admin.site.register(Salesman, SalesmanAdmin)

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["id","owner","name","description","price"]
admin.site.register(Product, ProductAdmin)

class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ["id","name"]
admin.site.register(City, CityAdmin)