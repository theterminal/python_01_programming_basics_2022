# 20220130 - Python Code
# Min Number
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
