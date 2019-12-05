# 1196.
import math

teacher_dates = []
same_dates = 0

n = int(input())

while n > 0:
    tdate = int(input())
    teacher_dates.append(tdate)
    n = n - 1
teacher_dates = list(dict.fromkeys(teacher_dates))

m = int(input())

while m > 0:
    sdate = int(input())
    L = 0
    R = len(teacher_dates) - 1

    while L <= R:
        x = math.floor((L + R) / 2)

        if teacher_dates[x] < sdate:
            L = x + 1
        if teacher_dates[x] > sdate:
            R = x - 1
        if teacher_dates[x] == sdate:
            same_dates = same_dates + 1
            L = R + 1

    m = m - 1

print(same_dates)