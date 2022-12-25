# 20220111 - Python - Programming Basics
# additional 04 - Vegetable Market - judge: https://judge.softuni.org/Contests/Practice/Index/1642#3
# pastebin: https://pastebin.com/h2fDbuQa


# user input
price_vegetables_bgn_per_kg = float(input())
price_fruits_bgn_per_kg = float(input())
vegetables_sold_kg = int(input())
fruits_sold_kg = int(input())
eur_to_bgn_ratio = 1.94


# calculations
sold_vegetables_bgn = vegetables_sold_kg * price_vegetables_bgn_per_kg
sold_fruits_bgn = fruits_sold_kg * price_fruits_bgn_per_kg
total_bgn = sold_vegetables_bgn + sold_fruits_bgn
total_eur = total_bgn / eur_to_bgn_ratio


# output
print(f'{total_eur:.2f}')
