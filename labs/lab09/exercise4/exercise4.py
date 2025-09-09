current_reading = int(input())
previous_reading = int(input())

first_20__cubic_meters = 0.57 # Cost per cubic meter for first 20 cubic meters
next_15_cubic_meters = 1.03  # Cost per cubic meter for next 15 cubic meters
above_35_cubic_meters = 1.40  # Cost per cubic meter above 35 cubic meters

consumption = current_reading - previous_reading
if consumption <= 20:
    water_cost = consumption * first_20__cubic_meters
elif consumption <= 35:
    water_cost = (20 * first_20__cubic_meters) + ((consumption - 20) * next_15_cubic_meters)    
else:
    water_cost = (20 * first_20__cubic_meters) + (15 * next_15_cubic_meters) + ((consumption - 35) * above_35_cubic_meters)

additional_fixed_charge = 10.00
total_bill = water_cost + additional_fixed_charge

print(consumption)
print(water_cost)
print(total_bill)