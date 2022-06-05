# 20220218 - Python Code - Balls
from math import floor

num_balls_entered = int(input())
total_points = counter_red = counter_orange = counter_yellow = counter_white = counter_black = counter_other = 0

for _ in range(num_balls_entered):
    color = input()

    if color == 'red':
        total_points += 5
        counter_red += 1
    elif color == 'orange':
        total_points += 10
        counter_orange += 1
    elif color == 'yellow':
        total_points += 15
        counter_yellow += 1
    elif color == 'white':
        total_points += 20
        counter_white += 1
    elif color == 'black':
        counter_black += 1
        total_points = floor((total_points / 2))
    else:
        counter_other += 1
        continue

print(f'Total points: {total_points}')
print(f'Red balls: {counter_red}')
print(f'Orange balls: {counter_orange}')
print(f'Yellow balls: {counter_yellow}')
print(f'White balls: {counter_white}')
print(f'Other colors picked: {counter_other}')
print(f'Divides from black balls: {counter_black}')
