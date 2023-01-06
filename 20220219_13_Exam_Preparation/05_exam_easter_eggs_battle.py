# 20220219 - Python - Programming Basics - Exam Preparation
# 05 - Easter Eggs Battle - https://judge.softuni.org/Contests/Practice/Index/1637#6


# user input
num_egs_1 = int(input())
num_egs_2 = int(input())


# calculations & results
winner_entered = input()

if winner_entered == "End of battle":
    print(f"Player one has {num_egs_1} eggs left.")
    print(f"Player two has {num_egs_2} eggs left.")
    quit()

while winner_entered != "End of battle":
    if winner_entered == "one":
        num_egs_2 -= 1
        if num_egs_2 == 0:
            print(f"Player two is out of eggs. Player one has {num_egs_1} eggs left.")
            quit()
    elif winner_entered == "two":
        num_egs_1 -= 1
        if num_egs_1 == 0:
            print(f"Player one is out of eggs. Player two has {num_egs_2} eggs left.")
            quit()

    winner_entered = input()
    if winner_entered == "End of battle":
        print(f"Player one has {num_egs_1} eggs left.")
        print(f"Player two has {num_egs_2} eggs left.")
