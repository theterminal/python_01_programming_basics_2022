# 20220130 - Python - For Loop
# Additional 04 - Grades - judge: https://judge.softuni.org/Contests/Practice/Index/1680#3


# user's input
num_students = int(input())


# additional elements
grade_200_299 = grade_300_399 = grade_400_499 = grade_500_600 = 0
num_students_200_299 = num_students_300_399 = num_students_400_499 = num_students_500_600 = 0
sum_grades = 0


# calculations
for i in range(num_students):
    grade_entered = float(input())
    sum_grades += grade_entered

    if grade_entered < 3:
        grade_200_299 += grade_entered
        num_students_200_299 += 1
    elif grade_entered < 4:
        grade_300_399 += grade_entered
        num_students_300_399 += 1
    elif grade_entered < 5:
        grade_400_499 += grade_entered
        num_students_400_499 += 1
    elif grade_entered >= 5:
        grade_500_600 += grade_entered
        num_students_500_600 += 1

students_500_600 = num_students_500_600 / num_students * 100
students_400_499 = num_students_400_499 / num_students * 100
students_300_399 = num_students_300_399 / num_students * 100
students_200_299 = num_students_200_299 / num_students * 100
sum_grades = grade_200_299 + grade_300_399 + grade_400_499 + grade_500_600
average_grade = sum_grades / num_students


# result
print(f"Top students: {students_500_600:.2f}%")
print(f"Between 4.00 and 4.99: {students_400_499:.2f}%")
print(f"Between 3.00 and 3.99: {students_300_399:.2f}%")
print(f"Fail: {students_200_299:.2f}%")
print(f"Average: {average_grade:.2f}")
