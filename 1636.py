# 1636

teams_time = input()

qxx_time = int(teams_time[:teams_time.find(' ')])
zzz_time = int(teams_time[teams_time.find(' ') + 1:])

tasks_time = input()

current_task_time = ''
lost_time = 0

for i in range(len(tasks_time)+1):
    if tasks_time[i:i+1] != ' ':
        if current_task_time == '0':
            current_task_time = ''
        current_task_time = current_task_time + tasks_time[i:i+1]
    else:
        lost_time = lost_time + int(current_task_time) * 20
        current_task_time = ''

# don't want to skip last iteration
if current_task_time != '':
    lost_time = lost_time + int(current_task_time) * 20

if (zzz_time - lost_time) < qxx_time:
    print('Dirty debug :(')
else:
    print('No chance.')

