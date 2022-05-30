# Python Code - AnimalType

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
