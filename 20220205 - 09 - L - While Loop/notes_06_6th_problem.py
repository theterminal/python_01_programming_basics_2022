# 20220205 - Python Code
# 6-th problem from lecture.
import sys

# user input
number = input()

# calculations & results
smallest = sys.maxsize

while number != "Stop":
    number = int(number)
    if number < smallest:
        smallest = number
    number = input()

print(f"{smallest:.0f}")

