# 1409. Два бандита

shots = input().split(' ')
shooter_1 = int(shots[0])
shooter_2 = int(shots[1])
targets = shooter_1 + shooter_2 - 1

out = str(targets - shooter_1) + ' ' + str(targets - shooter_2)
print(out)