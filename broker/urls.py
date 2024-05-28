from . import views
from django.urls import path

urlpatterns = [
    path('products/',views.products),
    path('product/<int:pk>',views.product),
    path('find_product/',views.find_product),
    
]