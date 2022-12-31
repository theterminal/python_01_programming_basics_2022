# 20220130 - Python - For Loop
# Note 05 - Odd / Even Sum


n = int(input())
number = sum_even = sum_odd = differance = 0

for i in range(1, n + 1):
    number = int(input())
    if i % 2 == 0:
        sum_even += number
    else:
        sum_odd += number

differance = abs(sum_even - sum_odd)

if sum_even == sum_odd:
    print(f"Yes, Sum = {sum_even}")
else:
    print(f"No, Diff = {differance}")
