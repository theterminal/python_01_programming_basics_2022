# 20220210 - Python - Nested Loops
# 01 - Number Pyramid - judge: https://judge.softuni.org/Contests/Compete/Index/2422#0


# user's input
num_entered = int(input())


# additional information
current_num = 0
all_printed = False


# result
for row in range(1, num_entered):
    for col in range(1, row + 1):
        current_num += 1
        if current_num > num_entered:
            all_printed = True
            break
        print(current_num, end=" ")
    print()
    if all_printed:
        break
