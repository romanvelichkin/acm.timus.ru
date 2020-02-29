# 1327. Предохранители
# solved

# you need you find ho many odd numbers between A and B (including both)
import math

a = int(input())
b = int(input())

if a % 2 != 0:
    a -= 1

result = math.ceil((b - a) / 2)
print(result)
