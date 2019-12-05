# 1353. Миллиардная Функция Васи


def sum_loop(max_num, current_num, current_sum, target_sum, loop_num, result):
    local_num_loop = loop_num
    local_result = result
    local_current_sum = current_sum
    local_current_num = current_num

    if local_num_loop < 9:
        local_num_loop += 1
        for i in range(max_num+1):
            local_current_num = local_current_num + ' ' + str(i)
            local_current_sum += i
            if local_current_sum == target_sum:
                local_result += 1
                print(local_current_num)
                print('TARGET SUM: ' + str(target_sum) + ' RESULT: ' + str(local_result))
                break
            else:
                sum_loop(max_num, local_current_num, local_current_sum, target_sum, local_num_loop, local_result)



target_sum = int(input())
if target_sum > 9:
    max_num = 9
else:
    max_num = target_sum

current_num = ''
current_sum = 0
loop_num = 0
result = 0




sum_loop(max_num, current_num, current_sum, target_sum, loop_num, result)

"""
s = int(input())
result = 0
for a in range (s):
    for b in range(s):
        for c in range(s):
            for d in range(s):
                for e in range(s):
                    for f in range(s):
                        for g in range(s):
                            for h in range(s):
                                for i in range(s):
                                   if a+b+c+d+e+f+g+h+i == s-1:
                                       print(str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(d) + ' ' +
                                             str(e) + ' ' + str(f) + ' ' + str(g) + ' ' + str(h) + ' ' + str(i))
                                       result += 1
print(result)
"""

"""
0 (s=1) = 1
1 (s=2) = 9
2 (s=3) = 45
3 (s=4) = 165
количество чисел от 1 до 999 999 999, чья сумма цифр равна S

1 and 73-80 - 9

0 0 0 0 0 0 0 0 0
9 9 9 9 9 9 9 9 9

if s

if s == 81:
    result = 1

if s == 1:
    result += 1

print(result)
"""
