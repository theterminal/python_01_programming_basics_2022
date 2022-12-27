# 20220120 - Python - Conditional Statements Advanced
# 03 - AnimalType - judge: https://judge.softuni.org/Contests/Compete/Index/2415#2


# user input
animal = input().lower()


# calculations & results
if animal == "dog":
    result = "mammal"
elif animal == "crocodile" or\
        animal == "tortoise" or\
        animal == "snake":
    result = "reptile"
else:
    result = "unknown"

print(result)
