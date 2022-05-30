# 20220130 - Python Code
# From the lecture - Left and Right Sum

n = int(input())

left_sum = right_sum = diff = 0

for i in range(1, n + 1):
    left_sum = left_sum + int(input())

for j in range(1, n + 1):
    right_sum = right_sum + int(input())

diff = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {diff}")
