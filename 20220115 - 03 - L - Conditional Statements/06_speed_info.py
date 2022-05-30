# 20220112 - Python Code - Speed Info

# user input
speed_entered = float(input())

# calculations & results
if speed_entered <= 10:
    print("slow")
elif 10 < speed_entered <= 50:
    print("average")
elif 50 < speed_entered <= 150:
    print("fast")
elif 150 < speed_entered <= 1000:
    print("ultra fast")
elif speed_entered > 1000:
    print("extremely fast")
