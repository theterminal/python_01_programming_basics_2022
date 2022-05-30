# 20220120 - Python Code - Cinema Ticket

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
