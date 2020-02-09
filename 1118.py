# 1118. Нетривиальные числа
# solved

import math

input_data = input().split(' ')

a = int(input_data[0])
b = int(input_data[1])
best_num = 0
best_triv = 0

if a == 1:
    print(1)
else:
    for i in range(b, a - 1, -1):
        curr_triv = 1
        div_amount = 1

        for j in range(2, round(math.sqrt(i))):
            if i % j == 0:
                curr_triv += j
                curr_triv += i / j
                bottom_divisor = i / j
                div_amount += 2

        # prime numbers are least trivial
        if div_amount == 1:
            best_num = i
            break

        curr_triv = curr_triv / i

        if best_num == 0:
            best_num = i
            best_triv = curr_triv
        else:
            if curr_triv < best_triv:
                best_triv = curr_triv
                best_num = i

    print(best_num)
