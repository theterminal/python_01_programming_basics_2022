# 20220210 - Python - Nested Loops
# 04 - Train The Trainers - judge: https://judge.softuni.org/Contests/Compete/Index/2422#3


# user's input
num_of_jury_members = int(input())
title_of_presentation = input()


# given information
sum_grades, grade_entered, sum_of_average_grades, counter_titles = 0, 0, 0, 0


# calculations & result
while title_of_presentation != "Finish":
    for current_jury_member in range(num_of_jury_members):
        grade_entered = float(input())
        sum_grades += grade_entered

    average_grade = sum_grades / num_of_jury_members
    print(F"{title_of_presentation} - {average_grade:.2f}.")
    sum_of_average_grades += average_grade
    counter_titles += 1
    grade_entered = sum_grades = 0
    title_of_presentation = input()

sum_of_average_grades = sum_of_average_grades / counter_titles
print(f"Student's final assessment is {sum_of_average_grades:.2f}.")
