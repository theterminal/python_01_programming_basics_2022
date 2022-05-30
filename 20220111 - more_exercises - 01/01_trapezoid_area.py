# 20220111 - Python Code - Trapezoid Area
# judge url: https://judge.softuni.org/Contests/Practice/Index/1642#0
# pastebin url: https://pastebin.com/00RLHYpa

# user input
base_a = float(input())
base_b = float(input())
height = float(input())

# calculations
area = (base_a + base_b) * height / 2

# output
print(f"{area:.2f}")
# print('{:.{}f}'.format(area, 2))  # standard formatting
