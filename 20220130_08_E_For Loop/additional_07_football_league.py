# 20220130 - Python - For Loop
# Additional 07 - Football League - judge: https://judge.softuni.org/Contests/Practice/Index/1680#6


# user's input
capacity_stadium = int(input())
number_fans = int(input())


# additional elements
sector = ""
fans_a, fans_b, fans_v, fans_g = 0, 0, 0, 0


# calculations
for i in range(number_fans):
    sector = input()

    if sector == "A":
        fans_a += 1
    elif sector == "B":
        fans_b += 1
    elif sector == "V":
        fans_v += 1
    elif sector == "G":
        fans_g += 1

percent_a_to_all = fans_a / number_fans * 100
percent_b_to_all = fans_b / number_fans * 100
percent_v_to_all = fans_v / number_fans * 100
percent_g_to_all = fans_g / number_fans * 100
percent_all_to_capacity = number_fans / capacity_stadium * 100


# result
print(f"{percent_a_to_all:.2f}%")
print(f"{percent_b_to_all:.2f}%")
print(f"{percent_v_to_all:.2f}%")
print(f"{percent_g_to_all:.2f}%")
print(f"{percent_all_to_capacity:.2f}%")
