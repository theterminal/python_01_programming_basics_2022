# 20220121 - Python - Conditional Statements Advanced
# 01 - Cinema - judge: https://judge.softuni.org/Contests/Compete/Index/2416#0


# user input
type_preview = input()
num_rows = int(input())
num_col = int(input())


# calculations & results
price = 0
all_tickets = num_rows * num_col

if type_preview == "Premiere":
    price = 12.00
elif type_preview == "Normal":
    price = 7.50
elif type_preview == "Discount":
    price = 5.00

sales = all_tickets * price
print(f"{sales:.2f}")
