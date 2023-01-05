# 20220208 - Python - Nested Loops
# 03 - Combinations - judge: https://judge.softuni.org/Contests/Compete/Index/2421#2


# user input
n = int(input())


# calculations & results
counter = 0

for x in range(0, n + 1):
    for y in range(0, n + 1):
        for z in range(0, n + 1):
            if x + y + z == n:
                counter += 1

print(counter)
