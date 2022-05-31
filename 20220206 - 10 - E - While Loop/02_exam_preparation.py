# 20220205 - Python Code
# Exam Preparation

# user input
num_fails_allowed = int(input())
name_problem = input()

# calculations & results
counter_problems, sum_score, average_score, counter_fails, last_problem = 0, 0, 0, 0, ""

while name_problem != "Enough":
    score = int(input())

    if score <= 4:
        counter_fails += 1

        if counter_fails == num_fails_allowed:
            print(f"You need a break, {num_fails_allowed} poor grades.")
            quit()

    counter_problems += 1
    sum_score += score
    last_problem = name_problem
    name_problem = input()

average_score = f"{(sum_score / counter_problems):.2f}"

print(f"Average score: {average_score}")
print(f"Number of problems: {counter_problems}")
print(f"Last problem: {last_problem}")
