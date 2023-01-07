# 20220219 - Python - Programming Basics - Pre-Exam
# 04 - Exam - judge: https://judge.softuni.org/Contests/Compete/Index/3351#3


# user information
num_students = int(input())


# calculations & results
counter_200_299, counter_300_399, counter_400_499, counter_500_more = 0, 0, 0, 0
grades_sum_of_all = 0

for student in range(num_students):
    grade_current_student = float(input())

    if 2.00 <= grade_current_student < 3.00:
        counter_200_299 += 1
    elif 3.00 <= grade_current_student < 4.00:
        counter_300_399 += 1
    elif 4.00 <= grade_current_student < 5.00:
        counter_400_499 += 1
    elif grade_current_student >= 5.00:
        counter_500_more += 1

    grades_sum_of_all += grade_current_student

percent_500_more = counter_500_more / num_students * 100
percent_400_499 = counter_400_499 / num_students * 100
percent_300_399 = counter_300_399 / num_students * 100
percent_200_299 = counter_200_299 / num_students * 100

grade_average = grades_sum_of_all / num_students

print(f"Top students: {percent_500_more:.2f}%")
print(f"Between 4.00 and 4.99: {percent_400_499:.2f}%")
print(f"Between 3.00 and 3.99: {percent_300_399:.2f}%")
print(f"Fail: {percent_200_299:.2f}%")
print(f"Average: {grade_average:.2f}")
