from . import view
from django.urls import path

urlpatterns = [
    # product
    path('brokers/',view.brokers),

]