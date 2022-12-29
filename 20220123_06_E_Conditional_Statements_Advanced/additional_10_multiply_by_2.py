# 20220123 - Python - Conditional Statements Advanced
# additional 10 - Multiply By 2


# user input
number = float(input())


# calculations & results
while number >= 0:
    result = f"{(number * 2):.2f}"
    print(f"Result: {result}")
    number = float(input())

print("Negative number!")
