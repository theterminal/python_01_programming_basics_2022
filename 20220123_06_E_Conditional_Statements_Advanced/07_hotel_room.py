# 20220121 - Python - Conditional Statements Advanced
# 07 - Hotel Room - judge: https://judge.softuni.org/Contests/Compete/Index/2416#6


# user input
month = input()
num_nights = int(input())


# calculations & results
cost_studio = 0
cost_apartment = 0

if month == "May" or month == "October":
    cost_studio = num_nights * 50.00
    cost_apartment = num_nights * 65.00
    if num_nights > 14:
        cost_studio *= 0.7
    elif num_nights > 7:
        cost_studio *= 0.95
elif month == "June" or month == "September":
    cost_studio = num_nights * 75.20
    cost_apartment = num_nights * 68.70
    if num_nights > 14:
        cost_studio *= 0.8
elif month == "July" or month == "August":
    cost_studio = num_nights * 76.00
    cost_apartment = num_nights * 77.00

if num_nights > 14:
    cost_apartment *= 0.9

cost_apartment = f"{cost_apartment:.2f}"
cost_studio = f"{cost_studio:.2f}"

print(f"Apartment: {cost_apartment} lv.")
print(f"Studio: {cost_studio} lv.")
