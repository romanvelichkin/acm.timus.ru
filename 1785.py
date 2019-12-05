# 1785. Трудности локализации

num = int(input())

if num >= 1000:
    print('legion')
elif num >= 500:
    print('zounds')
elif num >= 250:
    print('swarm')
elif num >= 100:
    print('throng')
elif num >= 50:
    print('horde')
elif num >= 20:
    print('lots')
elif num >= 10:
    print('pack')
elif num >= 5:
    print('several')
elif num >= 1:
    print('few')
