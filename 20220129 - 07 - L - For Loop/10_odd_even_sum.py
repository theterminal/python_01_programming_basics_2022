# 20220128 - Python Code - Odd and Even Sums

nums_to_enter = int(input())

odd_sum, even_sum, diff = 0, 0, 0

for i in range(nums_to_enter):
    if i % 2 == 0:
        odd_sum += int(input())
    else:
        even_sum += int(input())

diff = abs(odd_sum - even_sum)

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    print("No")
    print(f"Diff = {diff}")
