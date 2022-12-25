# 20220111 - Python - Programming Basics
# additional 10 - Weather Forecast - Part 2 - judge: https://judge.softuni.org/Contests/Practice/Index/1642#9
# pastebin: https://pastebin.com/0TGz6PjK


# user input
degrees = float(input())


# calculations & output
if 26.00 <= degrees <= 35.00:
    print("Hot")
elif 20.1 <= degrees <= 25.9:
    print("Warm")
elif 15.00 <= degrees <= 20.00:
    print("Mild")
elif 12.00 <= degrees <= 14.9:
    print("Cool")
elif 5.00 <= degrees <= 11.9:
    print("Cold")
else:
    print("unknown")
