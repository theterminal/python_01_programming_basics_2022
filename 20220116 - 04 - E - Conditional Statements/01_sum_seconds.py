# Python Code - Sum Seconds

# user input
man_1 = int(input())
man_2 = int(input())
man_3 = int(input())

# calculations & results
sum_seconds = man_1 + man_2 + man_3
minutes = sum_seconds // 60
seconds = sum_seconds % 60

print(f"{minutes}:{seconds:02d}")

# ------second way of formating the result-----------------------------------

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
