# If tested in judge MUST remove all text not asked for!!!
import math

# user's input
figure = input()

# calculations
if figure == 'square':
    side = float(input())
    area = side * side
elif figure == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif figure == 'circle':
    radius = float(input())
    area = (radius * radius) * math.pi
elif figure == 'triangle':
    side_a = float(input())
    h_to_a = float(input())
    area = side_a * h_to_a / 2
else:
    print('wrong entry')

# result
print(f'{area:.3f}')