# 20220128 - Python Code - Number Sequence
import sys

n_numbers = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize

for i in range(n_numbers):
    number = int(input())
    if i == 0:                                      # if this check is deleted (first iteration), judge will give error
        max_number = min_number = number
    if number < min_number:
        min_number = number
    elif number > max_number:
        max_number = number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
