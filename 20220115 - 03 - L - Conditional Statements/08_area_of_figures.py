# Python Code - Area Of Figures
import math

# user input
figure = input()
area = 0

# calculations & results
if figure == "square":
    side = float(input())
    area = side ** 2
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif figure == "circle":
    radius = float(input())
    area = math.pi * radius ** 2
elif figure == "triangle":
    side = float(input())
    h = float(input())
    area = side * h / 2

print(f"{area:.3f}")
