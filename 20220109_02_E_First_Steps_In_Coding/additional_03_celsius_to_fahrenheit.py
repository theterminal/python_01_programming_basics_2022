# 20220111 - Python - Programming Basics
# additional 03 - Celsius to Fahrenheit Converter - judge: https://judge.softuni.org/Contests/Practice/Index/1642#2
# pastebin: https://pastebin.com/iZz9aAfY


# user input
degrees_celsius = float(input())


# calculations
degrees_fahrenheit = (degrees_celsius * 1.8) + 32


# output
print(f"{degrees_fahrenheit:.2f}")
# print("{:.{}f}".format(degrees_fahrenheit, 2))          # standard formatting
