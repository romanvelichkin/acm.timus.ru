# 1177. Сопоставление с шаблоном

import re

strings_num = 15
stings_list = ["'abcde' like 'a'", "'abcde' like 'a%'", "'abcde' like '%a'",  "'abcde' like 'b'", "'abcde' like 'b%'",
               "'abcde' like '%b'", "'25%' like '_5[%]'", "'_52' like '[_]5%'", "'ab' like 'a[a-cdf]'", "'ad' like 'a[a-cdf]'",
               "'ab' like 'a[-acdf]'", "'a-' like 'a[-acdf]'", "'[]' like '[[]]'", "'''''' like '_'''", "'U' like '[^a-zA-Z0-9]'"
              ]
like_string = "' like '"

string_check = 1

for i in range(strings_num):
    #input_string = "'cat' like 'c_[[%_a]]_%t[][][[ttt]]t'"
    input_string = stings_list[i]
    like_pos = input_string.find(like_string)
    string = input_string[1:like_pos]
    template = input_string[like_pos + len(like_string):-1]

    template_parts_list = []
    diapason = 0
    skobki = 0
    start_of = 0
    for j in range(len(template)):

        #print('j = ', str(j))
        if template[j] == '[' and diapason == 0:
            diapason = 1
            template_part = template[start_of:j]
            #print(template_part)
            template_part = template_part.replace('%', '$')
            template_part = template_part.replace('_', '\\S')
            #print(template_part)
            template_parts_list.append(template_part)
            start_of = j

        if diapason == 1 and template[j] == '[':
            skobki += 1

        if diapason == 1 and template[j] == ']' and skobki > 0:
            skobki -= 1

        if diapason == 1 and template[j] == ']' and skobki == 0:
            diapason = 0
            template_part = template[start_of:j+1]
            #print(template_part)
            template_parts_list.append(template_part)
            start_of = j+1

        if j == len(template)-1:
            template_part = template[start_of:]
            #print(template_part)
            template_part = template_part.replace('%', '$')
            template_part = template_part.replace('_', '\\S')
            #print(template_part)
            template_parts_list.append(template_part)

    template = ''
    for j in range(len(template_parts_list)):
        template = template + template_parts_list[j]
    #print(template)

    print(input_string + ' = ' + string + like_string + template)
    if re.match(template, string):
        print('YES')
    else:
        print('NO')


