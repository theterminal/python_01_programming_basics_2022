# 20220123 - Python Code - Flowers

# user input
num_hrizantemi = int(input())
num_roses = int(input())
num_tulips = int(input())
season = input().lower()
is_holiday = input()

# calculations & results
amount_hrizantemi, amount_roses, amount_tulips, total = 0, 0, 0, 0

if season == "spring" or season == "summer":
    total = num_hrizantemi * 2 + num_roses * 4.10 + num_tulips * 2.50
else:
    total = num_hrizantemi * 3.75 + num_roses * 4.50 + num_tulips * 4.15

num_flowers = num_hrizantemi + num_roses + num_tulips

if is_holiday == "Y":
    total *= 1.15

if season == "spring" and num_tulips > 7:
    total *= 0.95
elif season == "winter" and num_roses >= 10:
    total *= 0.9

if num_flowers > 20:
    total *= 0.8

price = f"{(total + 2):.2f}"
print(price)
