# 20220121 - Python Code - Journey

# user input
budget = float(input())
season = input()

# calculations & results
money = 0
destination = ""
place = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        money = budget * 0.3
    else:
        place = "Hotel"
        money = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        money = budget * 0.4
    else:
        place = "Hotel"
        money = budget * 0.8
else:
    destination = "Europe"
    place = "Hotel"
    money = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{place} - {money:.2f}")
