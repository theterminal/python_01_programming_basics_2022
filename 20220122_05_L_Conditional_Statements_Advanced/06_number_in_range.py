# 20220120 - Python - Conditional Statements Advanced
# 06 - Number In Range - judge: https://judge.softuni.org/Contests/Compete/Index/2415#5


# user input
number = float(input())


# calculations & results
if -100 <= number <= 100 and number != 0:
    result = "Yes"
else:
    result = "No"

print(result)
