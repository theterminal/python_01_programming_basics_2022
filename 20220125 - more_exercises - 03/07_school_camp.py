# Python Code - School Camp

# user input
season = input().lower()
group_type = input().lower()
students = int(input())
nights = int(input())

# calculations & results
sport = ""
price = 0

if season == "winter":
    if group_type == "boys":
        sport = "Judo"
        price = 9.60
    elif group_type == "girls":
        sport = "Gymnastics"
        price = 9.60
    elif group_type == "mixed":
        sport = "Ski"
        price = 10
elif season == "spring":
    if group_type == "boys":
        sport = "Tennis"
        price = 7.20
    elif group_type == "girls":
        sport = "Athletics"
        price = 7.20
    elif group_type == "mixed":
        sport = "Cycling"
        price = 9.50
elif season == "summer":
    if group_type == "boys":
        sport = "Football"
        price = 15
    elif group_type == "girls":
        sport = "Volleyball"
        price = 15
    elif group_type == "mixed":
        sport = "Swimming"
        price = 20

price = students * nights * price
if students >= 50:
    price *= 0.5
elif students >= 20:
    price *= 0.85
elif students >= 10:
    price *= 0.95

print(f"{sport} {price:.2f} lv.")
