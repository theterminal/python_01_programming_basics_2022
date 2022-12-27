# 20220120 - Python - Conditional Statements Advanced
# 10 - Invalid Number - judge: https://judge.softuni.org/Contests/Compete/Index/2415#9


# -------------------- version 1 ------------------------


# user input
number = int(input())


# calculations & results
result = ""

if number != 0 and not (100 <= number <= 200):
    result = "invalid"

print(result)


# -------------------- version 2 ------------------------


# user's input
number = int(input())


# calculations & results
if not (100 <= number <= 200 or number == 0):
    result = "invalid"

print(result)
