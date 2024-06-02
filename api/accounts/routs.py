from . import view
from django.urls import path

urlpatterns = [
    # product
    path('brokers/',view.Brokers.as_view()),
    path('broker/<int:pk>',view.BrokerID.as_view()),

    path('salers/',view.Salers.as_view()),
    path('saler/<int:pk>',view.SalerID.as_view()),




]