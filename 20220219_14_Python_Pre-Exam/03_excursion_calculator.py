# 20220219 - Python - Programming Basics - Pre-Exam
# 03 - Excursion Calculator - judge: https://judge.softuni.org/Contests/Compete/Index/3351#2


# user information
num_people_entered = int(input())
season_entered = input()


# calculations & results
price = 0

if season_entered == "spring":
    if num_people_entered <= 5:
        price = 50.00
    else:
        price = 48.00
elif season_entered == "summer":
    if num_people_entered <= 5:
        price = 48.50
    else:
        price = 45.00
    price *= 0.85
elif season_entered == "autumn":
    if num_people_entered <= 5:
        price = 60.00
    else:
        price = 49.50
elif season_entered == "winter":
    if num_people_entered <= 5:
        price = 86.00
    else:
        price = 85.00
    price *= 1.08

price_total = num_people_entered * price
print(f"{price_total:.2f} leva.")
