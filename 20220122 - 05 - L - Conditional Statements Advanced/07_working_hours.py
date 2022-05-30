# 20220120 - Python Code - Working Hours

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
