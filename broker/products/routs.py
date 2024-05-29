from . import view

from django.urls import path

urlpatterns = [
    # product
    path('products/',view.products),
    path('product/<int:pk>',view.product),
    path('find_product/',view.find_product),
    
]