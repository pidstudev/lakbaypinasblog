# travelcost/views.py
from django.shortcuts import render
from .calculator import calculate_cost

def calculate_travel_cost(request):
    if request.method == 'POST':
        total_distance = float(request.POST.get('distance', 0))
        fuel_consumption = float(request.POST.get('fuel_consumption', 0))
        fuel_price = float(request.POST.get('fuel_price', 0))
        toll_fee = float(request.POST.get('toll_fee', 0))
        vehicle_rental_cost = float(request.POST.get('vehicle_rental_cost', 0))

        calculator_result = calculate_cost(total_distance, fuel_consumption, fuel_price, toll_fee, vehicle_rental_cost)

        return render(request, 'travelcost/travelcost.html', {'calculator_result': calculator_result})
    else:
        return render(request, 'travelcost/travelcost.html')

