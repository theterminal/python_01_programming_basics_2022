# 20220130 - Python Code
# 5-th problem from lecture.
import sys

# user input
number = input()
biggest = -sys.maxsize

# calculations & results
while number != "Stop":
    if float(number) > biggest:
        biggest = float(number)

    number = input()

print(f"{biggest:.0f}")
