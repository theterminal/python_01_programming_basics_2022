# 20220121 - Python - Conditional Statements Advanced
# 09 - Ski Trip


# user input
days = int(input())
type_room = input()
grade = input()


# calculations & results
nights = days - 1
price = 0
result = 0

if type_room == "room for one person":
    price = 18
elif type_room == "apartment":
    price = 25
    if nights < 9:
        price *= 0.7
    elif 9 <= nights <= 14:
        price *= 0.65
    else:
        price *= 0.5
elif type_room == "president apartment":
    price = 35
    if nights < 9:
        price *= 0.9
    elif 9 <= nights <= 14:
        price *= 0.85
    else:
        price *= 0.8

if grade == "positive":
    price *= 1.25
elif grade == "negative":
    price *= 0.9

cost = nights * price

print(f"{cost:.2f}")
