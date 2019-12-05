# 1654

code = input()
#code = 'wwstdaadierfflitzzz'
i = 0
current_symb = ''
next_symb = ''
result = ''

for i in range(len(code)):
    if code[i] != '':
        if len(result) < 1:
            result = result + code[i]
        else:
            if result[len(result) - 1] != code[i]:
                result = result + code[i]
            else:
                result = result[:-1]
print(result)