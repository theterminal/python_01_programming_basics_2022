# 20220114 - Python Code - Bonus Score

# user input
start_points = int(input())

# calculations & results
bonus_points, total_points = 0, 0

if start_points <= 100:
    bonus_points += 5
elif start_points > 1000:
    bonus_points = start_points * 0.1
else:
    bonus_points = start_points * 0.2

if start_points % 2 == 0:
    bonus_points += 1

if start_points % 10 == 5:
    bonus_points += 2

total_points = start_points + bonus_points

print(bonus_points)
print(total_points)
