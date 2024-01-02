# travelcost/urls.py
from django.urls import path
from .views import calculate_travel_cost

urlpatterns = [
    path('', calculate_travel_cost, name='calculate_travel_cost'),
]
