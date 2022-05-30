# 20220111 - Python Code - Celsius to Fahrenheit Converter
# judge url: https://judge.softuni.org/Contests/Practice/Index/1642#2
# pastebin url: https://pastebin.com/iZz9aAfY

# user input
degrees_celsius = float(input())

# calculations
degrees_fahrenheit = (degrees_celsius * 1.8) + 32

# output
print(f"{degrees_fahrenheit:.2f}")
# print("{:.{}f}".format(degrees_fahrenheit, 2))          # standard formatting
