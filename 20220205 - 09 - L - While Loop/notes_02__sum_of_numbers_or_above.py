# 20220130 - Python Code
# Sum of numbers or above

# user input
number_to_check_against = int(input("Enter the check number: "))

# calculations & results
sum_numbers = 0

while True:
    number_to_enter = int(input("Enter one of few number/s for to sum: "))
    sum_numbers += number_to_enter

    if sum_numbers >= number_to_check_against:
        break

print(f"the sum: {sum_numbers} is '=' or '>' than {number_to_check_against}")

# ------- lecture's version -------------------------------------------------

# It does NOT work for 0 and under!!!

# n = int(input())
# sum_1 = 0
# while sum_1 < n:
#     current_num = int(input())
#     sum_1 += current_num
#
# print(sum_1)
