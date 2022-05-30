# Python Code - Godzilla vs Kong

# user input
budget = float(input())
num_statists = int(input())
price_clothes_one_statist = float(input())

# calculations & results
cost = 0
decor = budget * 0.1

if num_statists > 150:
    price_clothes_one_statist *= 0.9

cost = num_statists * price_clothes_one_statist + decor
diff = abs(budget - cost)

if budget >= cost:
    print(f"Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print(f"Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
