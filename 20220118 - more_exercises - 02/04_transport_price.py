# Python Code - Transport Price

# user input
km_to_travel = int(input())
day_night = input()

# calculations & results
price = 0

if km_to_travel < 20:
    if day_night == "day":
        price = km_to_travel * 0.79 + 0.70
    else:
        price = km_to_travel * 0.90 + 0.70
elif 20 <= km_to_travel < 100:
    price = km_to_travel * 0.09
else:
    price = km_to_travel * 0.06

print(f"{price:.2f}")
