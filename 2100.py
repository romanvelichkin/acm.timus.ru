# 2100. Свадебный обед
# solved

invitations_num = int(input())

friends_total = 2

for i in range(invitations_num):
    friend_name = input()
    if friend_name.find('+') != -1:
        friends_total += 2
    else:
        friends_total += 1

if friends_total == 13:
    friends_total += 1

print(friends_total * 100)
