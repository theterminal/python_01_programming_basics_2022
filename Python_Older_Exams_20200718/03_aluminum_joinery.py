# 20220218 - Python - Programming Basics - Exam 20200718
# 03 - Aluminum Joinery - judge: https://judge.softuni.org/Contests/Practice/Index/2507#2


# user's input
number_windows_ordered = int(input())
type_windows_ordered = input()
delivery = input()


# additional elements
price = discount = 0


# calculations
if number_windows_ordered < 10:
    print("Invalid order")
    quit()
else:
    if type_windows_ordered == "90X130":

        if 30 < number_windows_ordered <= 60:
            discount = 0.95
        elif number_windows_ordered > 60:
            discount = 0.92
        else:
            discount = 1

        price = number_windows_ordered * 110 * discount

    elif type_windows_ordered == "100X150":

        if 40 < number_windows_ordered <= 80:
            discount = 0.94
        elif number_windows_ordered > 80:
            discount = 0.9
        else:
            discount = 1

        price = number_windows_ordered * 140 * discount

    elif type_windows_ordered == "130X180":

        if 20 < number_windows_ordered <= 50:
            discount = 0.93
        elif number_windows_ordered > 50:
            discount = 0.88
        else:
            discount = 1

        price = number_windows_ordered * 190 * discount

    elif type_windows_ordered == "200X300":

        if 25 < number_windows_ordered <= 50:
            discount = 0.91
        elif number_windows_ordered > 50:
            discount = 0.86
        else:
            discount = 1

        price = number_windows_ordered * 250 * discount

if delivery == "With delivery":
    price = price + 60

if number_windows_ordered > 99:
    price *= 0.96


# result
print(f"{price:.2f} BGN")
