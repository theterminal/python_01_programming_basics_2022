
# user's input
price_luggage_over_20_kg = float(input())
luggage_kg = float(input())
days_to_travel = int(input())
number_bags = int(input())

# calculations
if luggage_kg < 10:
    fee_to_pay = price_luggage_over_20_kg * 0.2
elif 10 <= luggage_kg <= 20:
    fee_to_pay = price_luggage_over_20_kg * 0.5
else:
    fee_to_pay = price_luggage_over_20_kg

if days_to_travel > 30:
    fee_to_pay *= 1.1
elif 7 <= days_to_travel <= 30:
    fee_to_pay *= 1.15
elif days_to_travel < 7:
    fee_to_pay *= 1.4

fee_to_pay *= number_bags

# result
print(f"The total price of bags is: {fee_to_pay:.2f} lv.")
