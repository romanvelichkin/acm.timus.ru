# 1881. Длинное условие задачи

stats = input().split(' ')

# кол-во строк на странице
h = int(stats[0])
# кол-во символов в строке
w = int(stats[1])
# кол-во вводимых слов
n = int(stats[2])

rows = 1
pages = 1
current_row = ''

while n > 0:
    word = input()
    if current_row == '':
        current_row = word
    else:
        if (len(current_row) + 1 + len(word)) <= w:
            current_row = current_row + ' ' + word
        else:
            current_row = word
            rows = rows + 1
    if rows > h:
            rows = 1
            pages = pages + 1

    n = n - 1

print(pages)
