# 20220215 - Python Code - Unique PIN Codes - judge url: https://judge.softuni.org/Contests/Practice/Index/1381#0

upper_limit_num_1 = int(input())
upper_limit_num_2 = int(input())
upper_limit_num_3 = int(input())

for i in range(1, upper_limit_num_1 + 1):
    if i % 2 != 0:
        continue

    for j in range(2, upper_limit_num_2 + 1):
        if not(j == 2 or j == 3 or j == 5 or j == 7):
            continue

        for k in range(1, upper_limit_num_3 + 1):
            if k % 2 != 0:
                continue

            print(f'{i} {j} {k}')
