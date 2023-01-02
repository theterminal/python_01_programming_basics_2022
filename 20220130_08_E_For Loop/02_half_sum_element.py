# 20220129 - Python - For Loop
# 02 - Half Sum Element - judge: https://judge.softuni.org/Contests/Compete/Index/2418#1

import sys


n_numbers = int(input())

max_num = -sys.maxsize
total = 0

for i in range(n_numbers):
    num_entered = int(input())

    if num_entered > max_num:
        max_num = num_entered

    total += num_entered

diff = abs(max_num - (total - max_num))

if diff == 0:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {diff}")
