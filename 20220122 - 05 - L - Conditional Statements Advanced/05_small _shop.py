# 20220120 - Python Code - Small Shop

# user input
product = input().lower()
town = input().lower()
quantity = float(input())

# calculations
result = 0

if town == "sofia":
    if product == "coffee":
        result = quantity * 0.50
    elif product == "water":
        result = quantity * 0.80
    elif product == "beer":
        result = quantity * 1.20
    elif product == "sweets":
        result = quantity * 1.45
    elif product == "peanuts":
        result = quantity * 1.60

elif town == "plovdiv":
    if product == "coffee":
        result = quantity * 0.40
    elif product == "water":
        result = quantity * 0.70
    elif product == "beer":
        result = quantity * 1.15
    elif product == "sweets":
        result = quantity * 1.30
    elif product == "peanuts":
        result = quantity * 1.50
else:
    if product == "coffee":
        result = quantity * 0.45
    elif product == "water":
        result = quantity * 0.70
    elif product == "beer":
        result = quantity * 1.10
    elif product == "sweets":
        result = quantity * 1.35
    elif product == "peanuts":
        result = quantity * 1.55

print(f"{result:.2f}")
