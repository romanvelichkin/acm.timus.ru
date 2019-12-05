# 2023. Дональд-почтальон
# solved

n = int(input())
pos = 0

case_dist = {'A': 0, 'P': 0, 'O': 0, 'R': 0,
             'B': 1, 'M': 1, 'S': 1,
             'D': 2, 'G': 2, 'J': 2, 'K': 2, 'T': 2, 'W': 2}
steps = 0
for i in range(n):
    first_letter = input()[:1]

    steps += abs(pos - case_dist[first_letter])
    pos = case_dist[first_letter]

print(steps)
