# 1496. Спамер
# solved

submits_num = int(input())
submits_list = []
spamers_list = []

for i in range(submits_num):
    submit = input()
    if submit not in submits_list:
        submits_list.append(submit)
    else:
        if submit not in spamers_list:
            spamers_list.append(submit)

for i in range(len(spamers_list)):
    print(spamers_list[i])