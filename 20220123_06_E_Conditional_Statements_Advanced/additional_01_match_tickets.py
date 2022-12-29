# 20220123 - Python - Conditional Statements Advanced
# additional 01 - Match Tickets


# user input
budget = float(input())
category = input()
num_people = int(input())


# calculations & results
tickets = 0
transport = 0

if category == "VIP":
    tickets = 499.99 * num_people
elif category == "Normal":
    tickets = 249.99 * num_people

if 1 <= num_people <= 4:
    transport = budget * 0.75
elif 5 <= num_people <= 9:
    transport = budget * 0.6
elif 10 <= num_people <= 24:
    transport = budget * 0.5
elif 25 <= num_people <= 49:
    transport = budget * 0.4
else:
    transport = budget * 0.25

total_cost = tickets + transport
diff = abs(budget - total_cost)

if budget >= total_cost:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
