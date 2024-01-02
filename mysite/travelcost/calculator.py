# travelcost/calculator.py
def calculate_cost(total_distance, fuel_consumption, fuel_price, toll_fee, vehicle_rental_cost):
    BASE_FUEL_CONSUMPTION_VALUE = 7  # 7 km/L default vehicle fuel consumption
    BASE_FUEL_PRICE = 65  # 65 pesos per liter current average price
    BASE_VEHICLE_RENT_COST = 4500  # 4500 pesos per day

    total_distance = total_distance if total_distance is not None else 0
    fuel_consumption = fuel_consumption if fuel_consumption is not None else BASE_FUEL_CONSUMPTION_VALUE
    fuel_price = fuel_price if fuel_price is not None else BASE_FUEL_PRICE
    toll_fee = toll_fee if toll_fee is not None else 0
    vehicle_rental_cost = vehicle_rental_cost if vehicle_rental_cost is not None else BASE_VEHICLE_RENT_COST

    estimated_total_cost = (((total_distance * 2) / fuel_consumption) * fuel_price) + toll_fee + vehicle_rental_cost

    calculator_result = {
        'total_distance': total_distance * 2,
        'fuel_consumption': fuel_consumption,
        'fuel_price': fuel_price,
        'toll_fee': toll_fee,
        'vehicle_rental_cost': vehicle_rental_cost,
        'estimated_total_cost': estimated_total_cost,
    }

    return calculator_result

