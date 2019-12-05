# 1877. Велосипедные коды

code_1 = input()
code_2 = input()

if code_1 == '0000':
    print('yes')
# первый код - четный
elif int(code_1) // 2 == int(code_1) / 2:
    print('yes')
# второй код - нечетный
elif int(code_2) // 2 != int(code_2) / 2:
    print('yes')
else:
    print('no')