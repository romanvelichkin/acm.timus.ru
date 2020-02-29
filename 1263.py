# 1263. Выборы
# solved

data = input().split(' ')
n = int(data[0])
m = int(data[1])
votes = {}

# fill dict with candidates
# to show candidates without votes
for i in range(1, n + 1):
    votes[i] = 0

# votes
for i in range(m):
    vote = int(input())
    votes[vote] += 1

for vote in votes:
    result = round(100 * votes[vote] / m, 2)
    print('%.2f' % result + '%')
