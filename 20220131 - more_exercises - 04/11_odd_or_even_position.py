# 20220130 - Python Code
# Odd or Even Position

import sys

# user's input
numbers_entered = int(input())

# additional elements
odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

# calculations
for i in range(1, numbers_entered + 1):
    number = float(input())

    if i % 2 != 0:
        odd_sum += number

        if number > odd_max:
            odd_max = number

        if number < odd_min:
            odd_min = number
    else:
        even_sum += number

        if number > even_max:
            even_max = number

        if number < even_min:
            even_min = number

# result
print(f"OddSum={odd_sum:.2f},")

if odd_min == sys.maxsize:
    print(f"OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")

if odd_max == -sys.maxsize:
    print(f"OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={even_sum:.2f},")

if even_min == sys.maxsize:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")

if even_max == -sys.maxsize:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")
