# 20220205 - Python Code
# 7-th problem from the lecture.

# user input
name_student = input()

# additional elements
fails, grades, sum_grades, average = 0, 1, 0, 0

# calculations & results
while grades <= 12:
    grade = float(input())

    if grade < 4:
        fails += 1

        if fails == 2:
            print(f"{name_student} has been excluded at {grades} grade!")
            quit()
    else:
        sum_grades += grade
        average = sum_grades / grades
        grades += 1

print(f"{name_student} graduated! Average grade: {average:.2f}")
