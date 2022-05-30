# Python Code - Toy Shop
import math

# user input
price_vacation = float(input())
num_puzzles = int(input())
num_talking_dolls = int(input())
num_plush_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

# calculations & results
total_amount_after_discount = 0
num_total_ordered = num_puzzles + num_talking_dolls + num_plush_bears + num_minions + num_trucks

amount_puzzles = num_puzzles * 2.60
amount_talking_dolls = num_talking_dolls * 3
amount_plush_bears = num_plush_bears * 4.10
amount_minions = num_minions * 8.20
amount_trucks = num_trucks * 2.00

total_amount = amount_puzzles + amount_talking_dolls + amount_plush_bears + amount_minions + amount_trucks

if num_total_ordered >= 50:
    total_amount *= 0.75

total_amount *= 0.9

diff = abs(total_amount - price_vacation)

if total_amount >= price_vacation:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
