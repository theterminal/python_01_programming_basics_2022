# Python Code - Operations Between Numbers

# user input
num_1 = int(input())
num_2 = int(input())
operation = input()

# calculations & results
result = 0

if num_2 == 0:
    print(f"Cannot divide {num_1} by zero")
    quit()

if operation == "/":
    result = num_1 / num_2
    result = f"{num_1} / {num_2} = {result:.2f}"
elif operation == "%":
    result = num_1 % num_2
    result = f"{num_1} % {num_2} = {result}"
elif operation == "+":
    result = num_1 + num_2
    if result % 2 == 0:
        even = "even"
    else:
        even = "odd"
    result = f"{num_1} {operation} {num_2} = {result} - {even}"
elif operation == "-":
    result = num_1 - num_2
    if result % 2 == 0:
        even = "even"
    else:
        even = "odd"
    result = f"{num_1} {operation} {num_2} = {result} - {even}"
elif operation == "*":
    result = num_1 * num_2
    if result % 2 == 0:
        even = "even"
    else:
        even = "odd"
    result = f"{num_1} {operation} {num_2} = {result} - {even}"

print(result)
