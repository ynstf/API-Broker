
from django.urls import path, include

urlpatterns = [
    # product
    path('',include('broker.products.routs')),

    path('',include('broker.accounts.routs')),

    
]