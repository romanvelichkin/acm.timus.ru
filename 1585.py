# 1585. Пингвины
# solved

n = int(input())
ping_num = {}

for i in range(n):
    ping = input()
    if ping not in ping_num:
        ping_num[ping] = 0
    ping_num[ping] += 1

print(max(ping_num, key=ping_num.get))
