# Python Code - Fuel Tank - Part 2 (version 2)

# user input
fuel_type = input()
fuel_l = float(input())
card = input()

# calculations & results
total = 0

if fuel_type == "Gas":
    if card == "Yes":
        total = fuel_l * (0.93 - 0.08)
    else:
        total = fuel_l * 0.93
elif fuel_type == "Gasoline":
    if card == "Yes":
        total = fuel_l * (2.22 - 0.18)
    else:
        total = fuel_l * 2.22
elif fuel_type == "Diesel":
    if card == "Yes":
        total = fuel_l * (2.33 - 0.12)
    else:
        total = fuel_l * 2.33

if 20 <= fuel_l <= 25:
    total *= 0.92
elif fuel_l > 25:
    total *= 0.9

print(f"{total:.2f} lv.")
