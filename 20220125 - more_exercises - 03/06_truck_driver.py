# 20220123 - Python Code - Truck Driver

# user input
season = input().lower()
km_per_month = float(input())

# calculations & results
drivers_pay = 0
per_km = 0

if season == "winter":
    if km_per_month <= 5000:
        per_km = 1.05
    elif 5000 < km_per_month <= 10000:
        per_km = 1.25
    elif km_per_month > 10000:
        per_km = 1.45
elif season == "summer":
    if km_per_month <= 5000:
        per_km = 0.90
    elif 5000 < km_per_month <= 10000:
        per_km = 1.10
    elif km_per_month > 10000:
        per_km = 1.45
else:
    if km_per_month <= 5000:
        per_km = 0.75
    elif 5000 < km_per_month <= 10000:
        per_km = 0.95
    elif km_per_month > 10000:
        per_km = 1.45

drivers_pay = km_per_month * per_km * 4 * 0.9
print(f"{drivers_pay:.2f}")
