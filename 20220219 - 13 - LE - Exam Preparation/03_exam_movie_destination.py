# Python Code - Movie Destination - https://judge.softuni.org/Contests/Practice/Index/1699#4

# user input
budget = float(input())
destination = input()
season = input()
num_days_to_film = int(input())

# calculations & results
cost_per_day_filming = 0

if season == "Winter":
    if destination == "Dubai":
        cost_per_day_filming = 45000
    elif destination == "Sofia":
        cost_per_day_filming = 17000
    elif destination == "London":
        cost_per_day_filming = 24000
elif season == "Summer":
    if destination == "Dubai":
        cost_per_day_filming = 40000
    elif destination == "Sofia":
        cost_per_day_filming = 12500
    elif destination == "London":
        cost_per_day_filming = 20250

total_cost = num_days_to_film * cost_per_day_filming

if destination == "Dubai":
    total_cost *= 0.7

if destination == "Sofia":
    total_cost *= 1.25

diff = abs(budget - total_cost)

if budget >= total_cost:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")
