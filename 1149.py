# 1149

n = int(input())
current_part = ''
result = ''

for i in range(1, n+1):

    new_part = 'sin(' + str(i)

    if i > 1:
        if (i - 1) % 2 == 0:  # even
            current_part = current_part + '+'
        if (i - 1) % 2 != 0:  # odd
            current_part = current_part + '-'

    current_part = current_part + new_part
    current_full = current_part

    for j in range(1, i+1):
        current_full = current_full + ')'

    if result == '':
        result = result + current_full + '+' + str(n - i + 1)
    else:
        result = result + ')' + current_full + '+' + str(n - i + 1)


for k in range(1, n):
    result = '(' + result

print(result)


