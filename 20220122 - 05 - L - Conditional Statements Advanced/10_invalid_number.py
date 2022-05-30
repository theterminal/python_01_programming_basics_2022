# Python Code - Invalid Number

# user input
number = int(input())

# calculations & results
result = ""

if number != 0 and not (100 <= number <= 200):
    result = "invalid"

print(result)

# ----------------another way of solving this problem is----------------------------------

# # user's input
# number = int(input())
#
# # calculations & results
# if not (100 <= number <= 200 or number == 0):
#     result = "invalid"
#
# print(result)
