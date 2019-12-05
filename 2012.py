# 2012. Про Гришу Н.

time_for_task = 45
tasks_total = 12
tasks_solved = int(input())

time_left = 4 * 60
tasks_left = tasks_total - tasks_solved

time_for_tasks_left = tasks_left * time_for_task

if time_left >= time_for_tasks_left:
    print('YES')
else:
    print('NO')