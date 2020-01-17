# 1068. Сумма
# solved

n = int(input())
n_range = abs(n) // 2

if n == 0:
    result = 1
elif n > 0:
    if n_range == n / 2:
        result = (1 + n) * n_range
    else:
        result = (1 + n) * n_range + int((1 + n) / 2)
else:
    if n_range == abs(n) / 2:
        result = (-1 + n) * n_range + 1
    else:
        result = (-1 + n) * n_range + int((1 + n) / 2)

print(result)







