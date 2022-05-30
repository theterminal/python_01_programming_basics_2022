# 20220120 - Python Code - Weekend Or Working Day

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
