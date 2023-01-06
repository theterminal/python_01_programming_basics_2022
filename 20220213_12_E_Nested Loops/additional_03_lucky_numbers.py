# 20220215 - Python - Nested Loops
# Additional 03 - Lucky Numbers - judge: https://judge.softuni.org/Contests/Practice/Index/1381#2


num_N = int(input())
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for m in range(1, 10):
                if (i + j == k + m) and num_N % (i + j) == 0:
                    print(f'{i}{j}{k}{m}', end=' ')
