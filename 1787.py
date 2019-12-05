# 1787. Поворот на МЕГУ

stats = input().split(' ')
cars_min = input().split(' ')

# кол-во машин проезжающих за минуту
k = int(stats[0])
# кол-во минут
n = int(stats[1])

i = 0
rest = 0
while i < n:
    rest = rest + int(cars_min[i]) - k
    if rest < 0:
        rest = 0
    i += 1

print(rest)

