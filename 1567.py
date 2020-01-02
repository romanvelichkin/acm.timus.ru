# 1567. SMS-спам
# solved

text_input = input()
abc = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
symbols = ('.', ',', '!')

result = 0

for i in range(len(text_input)):
    current_letter = text_input[i:i+1]
    if current_letter in abc:
        result += abc.index(current_letter) % 3 + 1
    elif current_letter in symbols:
        result += symbols.index(current_letter) % 3 + 1
    elif current_letter == ' ':
        result += 1

print(result)
