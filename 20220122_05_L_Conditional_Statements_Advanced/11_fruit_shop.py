# 20220120 - Python - Conditional Statements Advanced
# 11 - Fruit Shop (This is an elegant solution by using arrays) - judge: https://judge.softuni.org/Contests/Compete/Index/2415#10


# -------------------- version 1 ------------------------


# user input
fruit_entered = input().lower()
day_of_week = input().lower()
quantity = float(input())


# calculations & results
result = 0
fruits = ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]
days_in_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
prices_week_day = [2.50, 1.20, 0.85, 1.45, 2.70, 5.50, 3.85]
prices_weekend = [2.70, 1.25, 0.90, 1.60, 3.00, 5.60, 4.20]

if fruit_entered not in fruits:
    print("error")
    quit()
else:
    if day_of_week not in days_in_week:
        print("error")
        quit()
    else:
        if day_of_week == "saturday" or day_of_week == "sunday":
            for index, value in enumerate(fruits):
                if fruit_entered == value:
                    result = prices_weekend[index]
                    break
        else:
            for index, value in enumerate(fruits):
                if fruit_entered == value:
                    result = prices_week_day[index]
                    break

result *= quantity
print(f"{result:.2f}")


# -------------------- version 2 ------------------------


# user input
fruit = input().lower()
day_of_week = input().lower()
quantity = float(input())


# calculations & results
result = 0
fruits = ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]
days_in_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

if fruit not in fruits:
    print("error")
    quit()
else:
    if day_of_week not in days_in_week:
        print("error")
        quit()
    else:
        if day_of_week == "saturday" or day_of_week == "sunday":
            if fruit == "banana":
                result = 2.70
            elif fruit == "apple":
                result = 1.25
            elif fruit == "orange":
                result = 0.90
            elif fruit == "grapefruit":
                result = 1.60
            elif fruit == "kiwi":
                result = 3.00
            elif fruit == "pineapple":
                result = 5.60
            elif fruit == "grapes":
                result = 4.20
        else:
            if fruit == "banana":
                result = 2.50
            elif fruit == "apple":
                result = 1.20
            elif fruit == "orange":
                result = 0.85
            elif fruit == "grapefruit":
                result = 1.45
            elif fruit == "kiwi":
                result = 2.70
            elif fruit == "pineapple":
                result = 5.50
            elif fruit == "grapes":
                result = 3.85

result *= quantity
print(f"{result:.2f}")
