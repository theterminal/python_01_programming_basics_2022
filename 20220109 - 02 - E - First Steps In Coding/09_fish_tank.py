# 20220109 Python Code - Fish Tank
# judge url: https://judge.softuni.org/Contests/Compete/Index/2424#8
# pastebin url: https://pastebin.com/q4yYUEYT

# user input
length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent_taken = float(input())

# calculations
volume_cubic_cm = length_cm * width_cm * height_cm
volume_l = volume_cubic_cm * 0.001
liters = volume_l * (1 - (percent_taken / 100))

# output
print(f"{liters}")
