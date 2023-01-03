# 20220206 - Python - While Loop
# Additional 05 - Average Numbers - judge: https://judge.softuni.org/Contests/Practice/Index/1684#4


# user's input
numbers_entered = int(input())


# additional elements
total = 0
number = ""


# result
for i in range(1, numbers_entered + 1):
    number = int(input())
    total += number

print(f"{(total / numbers_entered):.2f}")
