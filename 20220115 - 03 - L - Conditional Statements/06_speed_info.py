# Python Code

# user input
speed = float(input())

# calculations & results
if speed <= 10:
    print("slow")
elif 10 < speed <= 50:
    print("average")
elif 50 < speed <= 150:
    print("fast")
elif 150 < speed <= 1000:
    print("ultra fast")
elif speed > 1000:
    print("extremely fast")
