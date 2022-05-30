# 20220129 - Python Code
# Histogram

nums_to_enter = int(input())

counter_p1 = counter_p2 = counter_p3 = counter_p4 = counter_p5 = 0

for i in range(nums_to_enter):
    num_entered = int(input())
    if num_entered < 200:
        counter_p1 += 1
    elif 200 <= num_entered < 400:
        counter_p2 += 1
    elif 400 <= num_entered < 600:
        counter_p3 += 1
    elif 600 <= num_entered < 800:
        counter_p4 += 1
    elif num_entered >= 800:
        counter_p5 += 1

percent_p1 = f"{(counter_p1 / nums_to_enter * 100):.2f}%"
percent_p2 = f"{(counter_p2 / nums_to_enter * 100):.2f}%"
percent_p3 = f"{(counter_p3 / nums_to_enter * 100):.2f}%"
percent_p4 = f"{(counter_p4 / nums_to_enter * 100):.2f}%"
percent_p5 = f"{(counter_p5 / nums_to_enter * 100):.2f}%"

print(percent_p1)
print(percent_p2)
print(percent_p3)
print(percent_p4)
print(percent_p5)
