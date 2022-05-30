# Python Code - Harvest
import math

# user input
size_land_sq_m = int(input())
grapes_from_1_sq_m_kg = float(input())
needed_wine_l = int(input())
num_workers = int(input())
for_1_l_wine_needed_kg = 2.5

# calculations & results
size_land_wine_sq_m = size_land_sq_m * 0.4
grapes_for_wine_kg = size_land_wine_sq_m * grapes_from_1_sq_m_kg
wine_from_grapes_for_wine_l = grapes_for_wine_kg / 2.5

diff = abs(needed_wine_l - wine_from_grapes_for_wine_l)
wine_per_worker = diff / num_workers

if wine_from_grapes_for_wine_l < needed_wine_l:
    print(f"It will be a tough winter! More {math.floor(diff)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(wine_from_grapes_for_wine_l)} liters.")
    print(f"{math.ceil(diff)} liters left -> {math.ceil(wine_per_worker)} liters per person.")
