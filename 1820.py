# 1820. Уральские бифштексы
import math

start_data = input().split(' ')

n = int(start_data[0])
k = int(start_data[1])

if n < k:
    result = 2
else:
    result = math.ceil((n*2) / k)

print(result)

