# 20220130 - Python - For Loop
# Note 03 - Biggest and Smallest Number

import sys


smallest = sys.maxsize
biggest = -sys.maxsize
nums_to_enter = int(input())

for i in range(0, nums_to_enter):
    num = int(input())
    if num < smallest:
        smallest = num
    if num > biggest:
        biggest = num

print(f"Max number: {biggest}")
print(f"Min number: {smallest}")
