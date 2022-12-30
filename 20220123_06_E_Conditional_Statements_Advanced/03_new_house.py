# 20220121 - Python - Conditional Statements Advanced
# 03 - New House - judge: https://judge.softuni.org/Contests/Compete/Index/2416#2


# ---------------------- version 2 -------------------------


# user input
flower = input()
num_flowers = int(input())
budget = int(input())


# calculations & results
price = 0

if flower == "Roses":
    price = 5
    if num_flowers > 80:
        price *= 0.9
elif flower == "Dahlias":
    price = 3.80
    if num_flowers > 90:
        price *= 0.85
elif flower == "Tulips":
    price = 2.80
    if num_flowers > 80:
        price *= 0.85
elif flower == "Narcissus":
    price = 3
    if num_flowers < 120:
        price *= 1.15
elif flower == "Gladiolus":
    price = 2.50
    if num_flowers < 80:
        price *= 1.2

cost = num_flowers * price
diff = abs(budget - cost)

if budget >= cost:
    print(f"Hey, you have a great garden with {num_flowers} {flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")


# ---------------------- version 1 -------------------------


# user's input
flower_entered = input()
number_flowers = int(input())
budget = int(input())

price_rose = 5
price_dahlia = 3.80
price_tulip = 2.80
price_narcissus = 3
price_gladiolus = 2.50

# calculations & results
result = 0
flower = flower_entered.lower()

if flower == "roses" and number_flowers > 80:
    result = number_flowers * price_rose * 0.9
elif flower == "roses":
    result = number_flowers * price_rose
if flower == "dahlias" and number_flowers > 90:
    result = number_flowers * price_dahlia * 0.85
elif flower == "dahlias":
    result = number_flowers * price_dahlia
if flower == "tulips" and number_flowers > 80:
    result = number_flowers * price_tulip * 0.85
elif flower == "tulips":
    result = number_flowers * price_tulip
if flower == "narcissus" and number_flowers < 120:
    result = number_flowers * price_narcissus * 1.15
elif flower == "narcissus":
    result = number_flowers * price_narcissus
if flower == "gladiolus" and number_flowers < 80:
    result = number_flowers * price_gladiolus * 1.2
elif flower == "gladiolus":
    result = number_flowers * price_gladiolus

if budget >= result:
    print(f"Hey, you have a great garden with {number_flowers} {flower_entered} and {(budget - result):.2f} leva left.")
else:
    print(f"Not enough money, you need {(result - budget):.2f} leva more.")
