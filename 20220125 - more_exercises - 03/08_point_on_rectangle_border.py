# Python Code - Point On Rectangle Border

# user input
x1, y1, x2, y2, x, y = float(input()), float(input()), float(input()), float(input()), float(input()), float(input())

# calculations & results
if (x1 <= x <= x2 and (y == y1 or y == y2)) or (y1 <= y <= y2 and (x == x1 or x == x2)):
    print("Border")
else:
    print("Inside / Outside")

# KK added ----------------------------------------------------------
x_coordinate = (x2 - x1 + 1) * 2
y_coordinate = (y2 - y1 + 1) * 2
all_points = x_coordinate + y_coordinate - 4

print(f"from rectangle x[{x1}:{x2}] and y[{y1}:{y2} ")
print(f"all points on the border are: {all_points:}")
