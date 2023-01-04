# 20220128 - Python - For Loop
# 09 - Left & Right Sums - judge: https://judge.softuni.org/Contests/Compete/Index/2417#9


nums_to_enter = int(input())
left_sum = right_sum = diff = 0

for i in range(nums_to_enter):
    left_sum += int(input())

for i in range(nums_to_enter):
    right_sum += int(input())

diff = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {diff}")
