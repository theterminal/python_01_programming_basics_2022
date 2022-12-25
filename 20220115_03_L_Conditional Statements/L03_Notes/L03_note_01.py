# 20220112 - Programming Basics - Conditional Statements
# If tested in judge MUST remove all text not asked for!!!

import math


# some math functions and their results...
a = float(input())
b = math.ceil(a)
c = math.floor(a)
d = round(a, 4)
e = int(a)
f = f'{a:.3f}'
g = abs(a)

print(f'math.ceil: {b}')
print(f'math.floor: {c}')  # TODO This how to to use TODO function and see it in the bottom window
print(f'round: {d}')
print(f'int: {e}')
print(f'(a:.3f): {f}')
print(f'abs: {g}')


# ----------------------------------------------------------------------------------


a = 12
b = int(input())

if a != b:
    print('a != b')
else:
    print('a is not b')


# -----------------------------------------------------------------------------------
