# 20220123 - Python Code - Car To Go

# user input
budget = float(input())
season = input().lower()

# calculations & results
car_class = ""
car_type = ""
price = 0

if budget <= 100:
    car_class = "Economy class"
    if season == "summer":
        car_type = "Cabrio"
        price = budget * 0.35
    elif season == "winter":
        car_type = "Jeep"
        price = budget * 0.65
elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "summer":
        car_type = "Cabrio"
        price = budget * 0.45
    elif season == "winter":
        car_type = "Jeep"
        price = budget * 0.8
elif budget > 500:
    car_class = "Luxury class"
    car_type = "Jeep"
    price = budget * 0.9

print(f"{car_class}")
print(f"{car_type} - {price:.2f}")
