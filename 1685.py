# 1685. Орфография

import math

#input_string = 'Vasya likes soup.'
input_string = '12345678'
string_len = len(input_string)
result = ''
string_list = []
string_list.append(input_string)

for i in range(string_len):
    current_string = string_list.pop()
    #print('current_string = ' + current_string)

    mid_position = math.ceil(len(current_string)/2) - 1
    #print('result = ' + result + ' + ' + current_string[mid_position])
    result = result + current_string[mid_position]

    if len(current_string) > 1:
        if len(current_string) >= 3:
            string_list.append(current_string[mid_position + 1:])
            #print(string_list)
            string_list.append(current_string[:mid_position])
            #print(string_list)
        elif len(current_string) < 3:
            string_list.append(current_string[1])
            #print(string_list)

print(result)

result_a = ''
string_list.clear
string_list.append(result)
replace_string = 'xxxxxxxx'
for i in range(string_len):

    current_string = string_list.pop()

    mid_position = math.ceil(len(replace_string)/2) - 1
    replace_string = replace_string[:mid_position] + current_string[i] + replace_string[mid_position + 1:]
    print('replace_string = ' + replace_string)

    if len(current_string) > 1:
        if len(current_string) >= 3:
            string_list.append(current_string[mid_position + 1:])
            #print(string_list)
            string_list.append(current_string[:mid_position])
            #print(string_list)
        elif len(current_string) < 3:
            string_list.append(current_string[1])
            #print(string_list)

print(result_a)