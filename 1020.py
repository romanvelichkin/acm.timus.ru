# 1020. Ниточка
# solved

import math

input_data = input().split()
corners_num = int(input_data[0])
radius = float(input_data[1])

x_coord_list = []
y_coord_list = []

for i in range(corners_num):
    input_data = input().split()
    x_coord_list.append(float(input_data[0]))
    y_coord_list.append(float(input_data[1]))

total_length = 0
vec_length = 0

for i in range(corners_num):
    if i < corners_num - 1:
        vec_a_x = x_coord_list[i + 1] - x_coord_list[i]
        vec_a_y = y_coord_list[i + 1] - y_coord_list[i]
    else:
        vec_a_x = x_coord_list[0] - x_coord_list[i]
        vec_a_y = y_coord_list[0] - y_coord_list[i]

    vec_length = math.sqrt(vec_a_x**2 + vec_a_y**2)

    total_length += vec_length

total_length += 2 * math.pi * radius
total_length = round(total_length, 2)
print(total_length)