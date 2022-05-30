# 20220129 - Python Code
# Trekking Mania

num_groups = int(input())

num_in_group_entered = num_musala = num_monblan = num_kilimanjaro = num_k2 = num_everest = 0

for i in range(num_groups):
    num_in_group_entered = int(input())
    if 0 <= num_in_group_entered <= 5:
        num_musala += num_in_group_entered
    elif 6 <= num_in_group_entered <= 12:
        num_monblan += num_in_group_entered
    elif 13 <= num_in_group_entered <= 25:
        num_kilimanjaro += num_in_group_entered
    elif 26 <= num_in_group_entered <= 40:
        num_k2 += num_in_group_entered
    elif num_in_group_entered >= 41:
        num_everest += num_in_group_entered

num_all = num_musala + num_monblan + num_kilimanjaro + num_k2 + num_everest

print(f"{(num_musala / num_all * 100):.2f}%")
print(f"{(num_monblan / num_all * 100):.2f}%")
print(f"{(num_kilimanjaro / num_all * 100):.2f}%")
print(f"{(num_k2 / num_all * 100):.2f}%")
print(f"{(num_everest / num_all * 100):.2f}%")
