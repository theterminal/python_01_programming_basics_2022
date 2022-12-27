# 20220120 - Python - Conditional Statements Advanced
# 02 - Weekend Or Working Day - judge: https://judge.softuni.org/Contests/Compete/Index/2415#1


# user input
day_entered = input().lower()


# calculations & results
if day_entered == "monday" or \
        day_entered == "tuesday" or \
        day_entered == "wednesday" or \
        day_entered == "thursday" or \
        day_entered == "friday":
    result = "Working day"
elif day_entered == "saturday" or day_entered == "sunday":
    result = "Weekend"
else:
    result = "Error"

print(result)
