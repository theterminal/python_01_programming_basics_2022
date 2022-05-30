# 20220121 - Python Code - Fishing Boat

# user input
budget = int(input())
season = input()
number_fishermen = int(input())

# calculations & results
rent = 0

if season == "Spring":
    rent = 3000
elif season == "Winter":
    rent = 2600
else:
    rent = 4200

if number_fishermen <= 6:
    rent *= 0.9
elif 7 < number_fishermen <= 11:
    rent *= 0.85
else:
    rent *= 0.75

if number_fishermen % 2 == 0 and season != "Autumn":
    rent *= 0.95

diff = abs(budget - rent)

if budget >= rent:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
