#string = input('Стока: ')
string = 'Машенька пишет Саше'
word = ''
words = []
for letter in string:
    if letter == ' ':
        words.append(word)
        word = ''
    else:
        word += letter
        if word == string[-len(word):]:
            words.append(word)
            word = ''
print('Строка:', string)
print('Самое длинное слово:', max(words, key=len))