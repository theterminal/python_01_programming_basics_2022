# 20220117 - Python Code - Pets
import math

# user input
number_days_travel = int(input())
total_food_available_for_the_vacation_kg = int(input())
dog_food_required_per_day_kg = float(input())
cat_food_required_per_day_kg = float(input())
turtle_food_required_per_day_kg = float(input()) * 0.001

# calculations & results
dog_food_total_required_kg = number_days_travel * dog_food_required_per_day_kg
cat_food_total_required_kg = number_days_travel * cat_food_required_per_day_kg
turtle_food_total_required_kg = number_days_travel * turtle_food_required_per_day_kg

total_food_required_kg = dog_food_total_required_kg + cat_food_total_required_kg + turtle_food_total_required_kg
diff = abs(total_food_required_kg - total_food_available_for_the_vacation_kg)

if total_food_available_for_the_vacation_kg >= total_food_required_kg:
    print(f"{math.floor(diff)} kilos of food left.")
else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")
