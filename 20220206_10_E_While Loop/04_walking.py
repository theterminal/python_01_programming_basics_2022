# 20220205 - Python - While Loop
# 04 - Walking - judge: https://judge.softuni.org/Contests/Compete/Index/2420#3


# user input
steps_entered = input()


# calculations & results
steps_total = 0
steps_to_home = 0

while True:
    if steps_entered == "Going home":
        steps_to_home = int(input())
        steps_total += steps_to_home

        if steps_total >= 10000:
            print("Goal reached! Good job!")
            print(f"{steps_total - 10000} steps over the goal!")
            break
        else:
            print(f"{10000 - steps_total} more steps to reach goal.")
            break
    else:
        steps_entered = int(steps_entered)
        steps_total += steps_entered

        if steps_total >= 10000:
            print("Goal reached! Good job!")
            print(f"{steps_total - 10000} steps over the goal!")
            exit()

    steps_entered = input()


# -------------------- version 2 ----------------------------


# user input
steps = input()


# calculations & result
total_steps = 0

if steps == "Going home":
    steps_to_home = int(input())
    if 10000 <= steps_to_home:
        print("Goal reached! Good job!")
        print(f"{abs(10000 - steps_to_home)} steps over the goal!")
        quit()
    else:
        print(f"{abs(10000 - steps_to_home)} more steps to reach goal.")
    quit()
else:
    total_steps = int(steps)

while total_steps < 10000:
    steps = input()

    if steps == "Going home":
        steps_to_home = int(input())
        total_steps += steps_to_home
        if total_steps >= 10000:
            print("Goal reached! Good job!")
            print(f"{abs(10000 - total_steps)} steps over the goal!")
        else:
            print(f"{abs(10000 - total_steps)} more steps to reach goal.")
        quit()
    total_steps += int(steps)

    if total_steps >= 10000:
        break

print("Goal reached! Good job!")
# print(f"{abs(10000 - total_steps)} steps over the goal!")
