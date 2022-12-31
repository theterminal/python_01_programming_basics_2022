# 20220128 - Python - For Loop
# 07 - Sum Numbers - judge: https://judge.softuni.org/Contests/Compete/Index/2417#6


n_numbers_to_enter = int(input())
total = 0

for i in range(n_numbers_to_enter):
    number = int(input())
    total += number

print(total)
