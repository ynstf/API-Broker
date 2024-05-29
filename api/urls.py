from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('city', views.CityViewsets)


urlpatterns = [
    # product
    path('',include('api.products.routs')),
    # accounts
    path('',include('api.accounts.routs')),

    # city
    path('', include(router.urls)),

    
]