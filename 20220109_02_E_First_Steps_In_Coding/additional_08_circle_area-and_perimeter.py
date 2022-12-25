# 20220111 - Python - Programming Basics
# additional 08 - Circle Area and Perimeter - judge: https://judge.softuni.org/Contests/Practice/Index/1642#7
# pastebin: https://pastebin.com/yZ3fZXA3

from math import pi                             # or can import math and use math.pi instead


# user input
radius = float(input())

# calculations
area = radius * radius * pi
perimeter = 2 * pi * radius

# output
print('{:.{}f}'.format(area, 2))
print('{:.{}f}'.format(perimeter, 2))
