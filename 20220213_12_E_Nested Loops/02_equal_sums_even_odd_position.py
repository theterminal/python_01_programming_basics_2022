# 20220210 - Python - Nested Loops
# 02 - Equal Sums Even Odd Position - judge: https://judge.softuni.org/Contests/Compete/Index/2422#1


# user's input
num_1_entered = int(input())
num_2_entered = int(input())

if num_1_entered > num_2_entered:
    num_temp = num_1_entered
    num_1_entered = num_2_entered
    num_2_entered = num_temp


# calculations & result
for num in range(num_1_entered, num_2_entered + 1):
    num_to_str = str(num)
    sum_num_on_even_position = sum_num_on_odd_position = 0

    for index, digit in enumerate(num_to_str):
        if index % 2 == 0:
            sum_num_on_odd_position += int(digit)
        else:
            sum_num_on_even_position += int(digit)

    if sum_num_on_even_position == sum_num_on_odd_position:
        print(num, end=" ")
