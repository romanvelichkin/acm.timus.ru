# 1123. Зарплата
import math
#input_salary = input()

#input_salary = '00001x20000'
input_salary = '123456789' #'123454321'
input_half_len = math.ceil(len(input_salary)/2)

center_num = ''

if len(input_salary) % 2 == 0:
    left_half = input_salary[:input_half_len - 1]
    left_num_end = input_salary[input_half_len - 1:input_half_len]
    right_num_end = input_salary[input_half_len:input_half_len + 1]
    print(left_half + ' ' + left_num_end + right_num_end)
else:
    left_half = input_salary[:input_half_len - 2]
    left_num_end = input_salary[input_half_len - 2:input_half_len - 1]
    center_num = input_salary[input_half_len - 1:input_half_len]
    right_num_end = input_salary[input_half_len:input_half_len + 1]
    print(left_half + ' ' + left_num_end + center_num + right_num_end)

# а что если не первое правое число больше, а последующие? короче надо больше вариантов, и подумать - все ли они будут решаться одинаково


