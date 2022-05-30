# 20220117 - Python Code - Fuel Tank

# user input
type_fuel = input()
fuel_in_tank_l = int(input())

# calculations & results
type_fuel = type_fuel.lower()

if type_fuel == "Diesel":
    if fuel_in_tank_l >= 25:
        print(f"You have enough {type_fuel}.")
    else:
        print(f"Fill your tank with {type_fuel}!")
elif type_fuel == "Gasoline":
    if fuel_in_tank_l >= 25:
        print(f"You have enough {type_fuel}.")
    else:
        print(f"Fill your tank with {type_fuel}!")
elif type_fuel == "Gas":
    if fuel_in_tank_l >= 25:
        print(f"You have enough {type_fuel}.")
    else:
        print(f"Fill your tank with {type_fuel}!")
else:
    print("Invalid fuel!")
