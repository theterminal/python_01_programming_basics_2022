# 20220130 - Python - While Loop
# 06 - Max Number - judge: https://judge.softuni.org/Contests/Compete/Index/2419#5

import sys


# user input
number = input()


# calculations & results
max_num = -sys.maxsize

while number != "Stop":
    number = int(number)

    if number > max_num:
        max_num = number

    number = input()

print(max_num)
