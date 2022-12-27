# 20220120 - Python - Conditional Statements Advanced
# 08 - Cinema Ticket - judge: https://judge.softuni.org/Contests/Compete/Index/2415#7


# user input
day_of_week = input().lower()


# calculations & results
if day_of_week == "wednesday" or day_of_week == "thursday":
    result = 14
elif day_of_week == "saturday" or day_of_week == "sunday":
    result = 16
else:
    result = 12

print(result)
