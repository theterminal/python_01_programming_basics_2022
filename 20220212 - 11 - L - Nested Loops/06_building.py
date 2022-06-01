# 20220208 - Python Code - Building

# user input
num_floors_entered = int(input())
num_rooms_per_floor = int(input())

# calculations & results
for floor_num in range(num_floors_entered, 0, -1):

    if floor_num == num_floors_entered:
        for room_num_last_floor in range(num_rooms_per_floor):
            print(f"L{floor_num}{room_num_last_floor}", end=" ")

    elif floor_num % 2 == 0 and floor_num != num_floors_entered:
        for room_num_even_floor in range(num_rooms_per_floor):
            print(f"O{floor_num}{room_num_even_floor}", end=" ")

    else:
        for room_num in range(num_rooms_per_floor):
            print(f"A{floor_num}{room_num}", end=" ")

    print()
