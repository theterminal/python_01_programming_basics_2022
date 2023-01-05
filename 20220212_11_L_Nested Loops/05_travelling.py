# 20220208 - Python - Nested Loops
# 05 - Travelling - judge: https://judge.softuni.org/Contests/Compete/Index/2421#4


total_saved = 0

while True:
    destination = input()

    if destination == "End":
        break

    minimum_budget = float(input())

    while True:
        saving = float(input())
        total_saved += saving

        if total_saved >= minimum_budget:
            print(f"Going to {destination}!")
            total_saved = 0
            break
