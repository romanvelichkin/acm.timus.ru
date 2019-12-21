# 1123. Зарплата
# solved

"""
If right half (reversed) less than left half, we reverse left half and replace the right one with it
If right half (reversed) is more than left half, we increase left half by 1 and replace it the right one with it

"""

import math

input_salary = input()
input_half_len = math.ceil(len(input_salary)/2)
equal_halves = 0
center_num = ''
result = ''

# for salary between 0 and 99
if len(input_salary) == 1:
    result = input_salary
elif len(input_salary) == 2:
    if int(input_salary[0]) <  int(input_salary[1]):
        result = str(int(input_salary[0]) + 1) + str(int(input_salary[0]) + 1)
    elif int(input_salary[0]) >  int(input_salary[1]):
        result = input_salary[0] + input_salary[0]
    else:
        result = input_salary

# for the rest
else:
    if len(input_salary) % 2 == 0:
        even_digits = 1
        left_half = input_salary[:input_half_len]
        right_half = input_salary[input_half_len:]
    else:
        even_digits = 0
        left_half = input_salary[:input_half_len - 1]
        center_num = input_salary[input_half_len - 1:input_half_len]
        right_half = input_salary[input_half_len:]

    for i in range(len(left_half)):

        if right_half[i] < left_half[-i - 1]:
            right_half = left_half[::-1]
            if even_digits == 1:
                result = left_half + right_half
            else:
                result = left_half + center_num + right_half
            equal_halves = 0
            break

        elif right_half[i] > left_half[-i - 1]:
            if even_digits == 1:
                left_half = str(int(left_half) + 1)
                right_half = left_half[::-1]
                result = left_half + right_half
            else:
                left_half = str(int(left_half)*10 + int(center_num) + 1)
                right_half = (left_half[::-1])[1:]
                result = left_half + right_half
            equal_halves = 0
            break

        else:
            equal_halves = 1

if equal_halves == 1:
    result = input_salary

print(result)



