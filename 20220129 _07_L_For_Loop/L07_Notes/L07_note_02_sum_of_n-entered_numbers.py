# 20220130 - Python - For Loop
# Note 02 - Sum of 'n' entered numbers


num_to_enter = int(input("How many numbers will be entered? "))
number = total = 0
number_entered = ""

for i in range(num_to_enter):
    number = int(input(f"Enter a number to add to the total: "))
    total += number
    print(f'So far you\'ve entered {i + 1} numbers and the Sub Total is: {total}')

print(f'Grand Total is: {total}')
