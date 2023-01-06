# 20220210 - Python - Nested Loops
# 05 - Special Numbers - judge: https://judge.softuni.org/Contests/Compete/Index/2422#4


# user input
num_entered = int(input())


# calculations & results
for current_num in range(1111, 10000):
    is_special = True
    current_num_as_str = str(current_num)

    for digit in current_num_as_str:
        if int(digit) == 0 or num_entered % int(digit) != 0:
            is_special = False
            break

    if is_special:
        print(current_num, end=" ")
