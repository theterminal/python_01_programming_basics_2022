# 20220130 - Python Code
# Equal Pairs

# user's input
number_pairs = int(input())

# additional elements
number = sum_pair = sum_pair_max = sum_pair_min = diff_max = 0

# calculations
for i in range(number_pairs * 2):
    number = int(input())
    sum_pair += number

    if i % 2 != 0 and i != 0:

        if i == 1:
            sum_pair_max = sum_pair_min = sum_pair

        if sum_pair >= sum_pair_max:
            sum_pair_max = sum_pair
            sum_pair = 0
        else:
            sum_pair_min = sum_pair
            sum_pair = 0

        diff = abs(sum_pair_max - sum_pair_min)

        if diff >= diff_max:
            diff_max = diff


if sum_pair_max == sum_pair_min:
    print(f"Yes, value={sum_pair_max}")
else:
    print(f"No, maxdiff={diff_max}")
