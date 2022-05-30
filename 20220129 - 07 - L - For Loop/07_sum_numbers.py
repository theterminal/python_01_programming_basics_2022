# 20220128 - Python Code - Sum Numbers

n_numbers_to_enter = int(input())
total = 0

for i in range(n_numbers_to_enter):
    number = int(input())
    total += number

print(total)
