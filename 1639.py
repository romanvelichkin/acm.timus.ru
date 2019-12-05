# 1639. Шоколад 2
# solved

m_n = input().split(' ')

m = int(m_n[0])
n = int(m_n[1])

if m*n / 2 == m*n // 2:
    print('[:=[first]')
else:
    print('[second]=:]')

