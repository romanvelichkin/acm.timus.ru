# 1014. Произведение цифр
# solved

n = int(input())
result = ''

if n == 0:
    result = '10'
elif n == 1:
    result = '1'
else:
    q = 0
    p = 1

    for i in range (9, 1, -1):
        while n%i == 0:
            q += p * i
            p = p * 10
            n = n / i
    if n == 1:
        result = str(q)
    else:
        result = '-1'

print(result)

