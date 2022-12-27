# 20220120 - Python - Conditional Statements Advanced
# 07 - Working Hours - judge: https://judge.softuni.org/Contests/Compete/Index/2415#6


# user input
hour_entered = int(input())
day_of_week = input().lower()


# calculations & results
result = 0

if day_of_week == "sunday" or (10 > hour_entered or hour_entered > 18):
    result = "closed"
else:
    result = "open"

print(result)
