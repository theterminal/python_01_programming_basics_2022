# 20220120 - Python - Conditional Statements Advanced
# 04 - Personal Titles - judge: https://judge.softuni.org/Contests/Compete/Index/2415#3


# ------------------------ version 1 ---------------------------------


# user input
age = float(input())
gender = input().lower()


# calculations & results
if 0 < age < 16:
    if gender == "m":
        result = "Master"
    else:
        result = "Miss"
else:
    if gender == "m":
        result = "Mr."
    else:
        result = "Ms."

print(result)


# ------------------------ version 2 ---------------------------------


# user input
age = float(input())
gender = input()


# calculations
if age < 16 and gender == "m":
    result = "Master"
elif age < 16 and gender == "f":
    result = "Miss"
elif age >= 16 and gender == "m":
    result = "Mr."
else:
    result = "Ms."


# result
print(result)
