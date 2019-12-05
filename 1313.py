# 1313. К вопросу о спорте
# solved

n = int(input())
list_of_strings = []
result = ''
x = 0

for i in range(n):
    list_of_strings.append(input().split(' '))

    for j in range(0, i+1):
        result = result + list_of_strings[i-j][j] + ' '

for i in range(n, n*2):
    x += 1

    for j in range(x, i+1 - x):
        result = result + list_of_strings[i-j][j] + ' '

print(result[:len(result)-1])

