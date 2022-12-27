# 20220120 - Python - Conditional Statements Advanced
# 01 - Day of Week - judge: https://judge.softuni.org/Contests/Compete/Index/2415#0


# user input
number = int(input())


# calculations & results
if number == 1:
    result = "Monday"
elif number == 2:
    result = "Tuesday"
elif number == 3:
    result = "Wednesday"
elif number == 4:
    result = "Thursday"
elif number == 5:
    result = "Friday"
elif number == 6:
    result = "Saturday"
elif number == 7:
    result = "Sunday"
else:
    result = "Error"

print(result)
