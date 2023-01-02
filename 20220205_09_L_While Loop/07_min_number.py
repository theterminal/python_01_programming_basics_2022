# 20220130 - Python - While Loop
# 07 - Min Number - judge: https://judge.softuni.org/Contests/Compete/Index/2419#6

import sys


# user input
number = input()


# calculations & results
min_num = sys.maxsize

while number != "Stop":
    number = int(number)

    if number < min_num:
        min_num = number

    number = input()

print(min_num)
