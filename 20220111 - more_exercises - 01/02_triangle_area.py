# 20220111 - Python Code - Triangle Area
# judge url: https://judge.softuni.org/Contests/Practice/Index/1642#1
# pastebin url: https://pastebin.com/fNPkQfpB

# user input
side_a = float(input())
height = float(input())

# calculations
area = side_a * height / 2

# output
print(f"{area:.2f}")
# print('{:.{}f}'.format(area, 2))  # standard formatting
