# 20220120 - Python - Conditional Statements Advanced
# 09 - Fruit Or Vegetable (simple solution but not elegant) - judge: https://judge.softuni.org/Contests/Compete/Index/2415#8


# -------------------- version 1 ------------------------


# user input
product = input()


# calculations & results
result = ""

if product == "banana" or\
        product == "apple" or \
        product == "kiwi" or \
        product == "cherry" or \
        product == "lemon" or \
        product == "grapes":
    result = "fruit"
elif product == "tomato" or \
        product == "cucumber" or \
        product == "pepper" or \
        product == "carrot":
    result = "vegetable"
else:
    result = "unknown"

print(result)


# -------------------- version 2 ------------------------


# user input
product = input()


# calculations & results
result = ""
flag = False
fruits = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
vegetables = ["tomato", "cucumber", "pepper", "carrot"]

for i in fruits:
    if i == product:
        result = "fruit"
        break
    for j in vegetables:
        if j == product:
            result = "vegetable"
            flag = True
            break
    if flag:
        break
    else:
        result = "unknown"

print(result)
