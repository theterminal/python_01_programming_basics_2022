# Python Code - Flower Shop
import math

# user input
num_magnolii = int(input())
num_ziumbiuli = int(input())
num_roses = int(input())
num_kaktusi = int(input())
price_gift = float(input())

# caclculations & resutlts
amount_magnolii = num_magnolii * 3.25
amount_ziumbiuli = num_ziumbiuli * 4
amount_roses = num_roses * 3.50
amount_kaktusi = num_kaktusi * 8

total = amount_magnolii + amount_ziumbiuli + amount_roses + amount_kaktusi

total *= 0.95

diff = abs(total - price_gift)

if total >= price_gift:
    print(f"She is left with {math.floor(diff)} leva.")
else:
    print(f"She will have to borrow {math.ceil(diff)} leva.")
