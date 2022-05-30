# 20220112 - Python Code - Area of Figures
import math

# user's input
figure_type = input()
area = 0

# calculations
if figure_type == 'square':
    side = float(input())
    area = side * side
elif figure_type == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif figure_type == 'circle':
    radius = float(input())
    area = (radius * radius) * math.pi
elif figure_type == 'triangle':
    side_a = float(input())
    h_to_a = float(input())
    area = side_a * h_to_a / 2
else:
    print('wrong entry')

# result
print(f'{area:.3f}')
