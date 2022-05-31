# 20220130 - Python Code
# Graduation

# user input
student_name_entered = input()

# calculations & results
grade_level, counter_fail, sum_grades, average_grade = 1, 0, 0, 0

while grade_level <= 12:
    grade_entered = float(input())

    if grade_entered < 4.00:
        counter_fail += 1

        if counter_fail == 2:
            print(f"{student_name_entered} has been excluded at {grade_level} grade")
            quit()

    else:
        grade_level += 1
        counter_fail = 0
        sum_grades += grade_entered

average_grade = f"{(sum_grades / 12):.2f}"
print(f"{student_name_entered} graduated. Average grade: {average_grade}")
