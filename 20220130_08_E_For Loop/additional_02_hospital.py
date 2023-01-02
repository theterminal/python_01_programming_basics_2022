# 20220130 - Python - For Loop
# Additional 02 - Hospital - judge: https://judge.softuni.org/Contests/Practice/Index/1680#1


# user's input
period = int(input())


# additional elements
treated = 0
untreated = 0
doctors = 7


# calculations
for i in range(1, period + 1):
    number_patients = int(input())

    if i % 3 == 0:
        if untreated > treated:
            doctors += 1

    if number_patients <= doctors:
        treated += number_patients
    else:
        treated += doctors
        untreated = untreated + (number_patients - doctors)


# result
print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")
