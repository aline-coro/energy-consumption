# Program to calculate an estimate for energy consumption and cost
# Author: Aline Coro
# Date: 22/03/2026

# Input
appliance_name = input("Type the name of an appliance (example: Refrigerator): ")
appliance_power = float(input("Type the appliance's power in watts (example: 100): "))
appliance_usage = float(input("What's the average daily usage in hours (example: 12.5)? "))
appliance_energycost = float(input("What's the cost per kWh (example: 0.75)? "))

# Processing
monthly_consumption = (appliance_power * appliance_usage * 30) / 1000
monthly_cost = monthly_consumption * appliance_energycost

# Output
print(f"\nAppliance: {appliance_name}")
print(f"Estimated energy consumption: {monthly_consumption:.2f} kWh/month")
print(f"Estimated cost: R${monthly_cost:.2f}/month")