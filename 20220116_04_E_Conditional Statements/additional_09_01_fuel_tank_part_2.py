# 20220117 - Python - Programming Basics - Conditional Statements
# additional 09_01 - Fuel Tank - Part 2 (version 1)


result = 0


# user's input
fuel_type = input()
fuel_l = float(input())
with_card = input()


# problem information
gasoline_lv_per_l = 2.22
diesel_lv_per_l = 2.33
gas_lv_per_l = 0.93


# calculations
total_gasoline_lv = gasoline_lv_per_l * fuel_l
total_diesel_lv = diesel_lv_per_l * fuel_l
total_gas_lv = gas_lv_per_l * fuel_l

if fuel_type == "Gasoline":
    if with_card == "Yes":
        if 20 < fuel_l <= 25:
            result = (total_gasoline_lv - fuel_l * 0.18) * 0.92
        elif fuel_l > 25:
            result = (total_gasoline_lv - fuel_l * 0.18) * 0.90
        else:
            result = total_gasoline_lv - fuel_l * 0.18
    elif with_card == "No":
        if 20 < fuel_l <= 25:
            result = total_gasoline_lv * 0.92
        elif fuel_l > 25:
            result = total_gasoline_lv * 0.90
        else:
            result = total_gasoline_lv
    else:
        print("Invalid card entry!")
elif fuel_type == "Diesel":
    if with_card == "Yes":
        if 20 < fuel_l <= 25:
            result = (total_diesel_lv - fuel_l * 0.12) * 0.92
        elif fuel_l > 25:
            result = (total_diesel_lv - fuel_l * 0.12) * 0.90
        else:
            result = total_diesel_lv - fuel_l * 0.12
    elif with_card == "No":
        if 20 < fuel_l <= 25:
            result = total_diesel_lv * 0.92
        elif fuel_l > 25:
            result = total_diesel_lv * 0.90
        else:
            result = total_diesel_lv
    else:
        print("Invalid card entry!")
elif fuel_type == "Gas":
    if with_card == "Yes":
        if 20 < fuel_l <= 25:
            result = (total_gas_lv - fuel_l * 0.08) * 0.92
        elif fuel_l > 25:
            result = (total_gas_lv - fuel_l * 0.08) * 0.90
        else:
            result = total_gas_lv - fuel_l * 0.08
    elif with_card == "No":
        if 20 < fuel_l <= 25:
            result = total_gas_lv * 0.92
        elif fuel_l > 25:
            result = total_gas_lv * 0.90
        else:
            result = total_gas_lv
    else:
        print("Invalid card entry!")
else:
    print("Invalid fuel type entry!")


# result
print(f'{result:.2f} lv.')
