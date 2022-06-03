# 20220219 - Python Code - Family Trip - https://judge.softuni.org/Contests/Practice/Index/1745#1

# user input
budget_entered = float(input())
num_nights_entered = int(input())
price_per_night = float(input())
percent_additional_expenses = int(input()) * 0.01

# calculations & results
if num_nights_entered > 7:
    price_per_night *= 0.95

amount_hotel = num_nights_entered * price_per_night
additional_expenses = percent_additional_expenses * budget_entered

total_needed = amount_hotel + additional_expenses
diff = abs(budget_entered - total_needed)

if budget_entered >= total_needed:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")
