# 20220111 - Python Code - House Painting
# judge url: https://judge.softuni.org/Contests/Practice/Index/1642#6
# pastebin url: https://pastebin.com/LArWAR7a

# user input
house_height_m = float(input())
house_width_m = float(input())
roof_height_m = float(input())

# calculations
walls_short_sq_m = (house_height_m ** 2) * 2 - (2 * 1.2)
walls_long_sq_m = (house_height_m * house_width_m) * 2 - (1.5 * 1.5) * 2
total_walls_sq_m = walls_short_sq_m + walls_long_sq_m

green_paint_l = total_walls_sq_m / 3.4

roof_rectangles_sq_m = (house_width_m * house_height_m) * 2
roof_triangles_sq_m = house_height_m * roof_height_m
total_roof_sq_m = roof_rectangles_sq_m + roof_triangles_sq_m

red_paint_l = total_roof_sq_m / 4.3

# output
print('{:.{}f}'.format(green_paint_l, 2))
print('{:.{}f}'.format(red_paint_l, 2))

# -------------------------- first solution---------------------------------------

# x = 6
# y = 10
# h = 5.2
#
# walls = (((2 * x * x) - (2 * 1.2)) + 2 * ((x * y) - (1.5 * 1.5))) / 3.4
# roof = (2 * ((x * y) + (x * h / 2))) / 4.3
#
# print(f"Green paint: {walls:.2f}")
# print(f"Red paint: {roof:.2f}")
