# 2066. Простое выражение

a = int(input())
b = int(input())
c = int(input())

if b*c > b+c:
    result = a - b*c
else:
    result = a - b - c

print(result)