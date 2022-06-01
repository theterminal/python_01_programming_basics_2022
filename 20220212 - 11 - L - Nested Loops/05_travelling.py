# 20220208 - Python Code - Travelling

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
