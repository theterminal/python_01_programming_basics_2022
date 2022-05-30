# 20220129 - Python Code
# Tennis Rank-list
import math

num_tournaments = int(input())
points_starting = int(input())

points_total = counter_w = 0

for i in range(num_tournaments):
    level_entered = input()
    if level_entered == "W":
        points_total += 2000
        counter_w += 1
    elif level_entered == "F":
        points_total += 1200
    elif level_entered == "SF":
        points_total += 720

points_final = points_starting + points_total
points_average = f"{math.floor(points_total / num_tournaments)}"
percent_won = f"{(counter_w / num_tournaments * 100):.2f}%"

print(f"Final points: {points_final}")
print(f"Average points: {points_average}")
print(percent_won)
