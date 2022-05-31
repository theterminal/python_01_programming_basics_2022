# 20220205 - Python Code
# Moving

# user input
axis_x, axis_y, axis_z = int(input()), int(input()), int(input())

# calculations & results
space_total = axis_x * axis_y * axis_z
space_left = space_total

while True:
    boxes_to_move_entered = input()

    if boxes_to_move_entered == "Done":
        print(f"{space_left} Cubic meters left.")
        break
    else:
        space_left -= int(boxes_to_move_entered)

        if space_left <= 0:
            print(f"No more free space! You need {abs(space_left)} Cubic meters more.")
            break
