
from django.urls import path, include

urlpatterns = [
    # product
    path('',include('broker.products.routs')),
    # accounts
    path('',include('broker.accounts.routs')),

    
]