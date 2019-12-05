# 1545. Иероглифы
# solved

n = int(input())
letter_list = []

for i in range(n):
    letter_list.append(input())

latin_letter = input()

for i in range(n):
    if letter_list[i][:1] == latin_letter:
        print(letter_list[i])