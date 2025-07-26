import json

# d = {'black': 'черный',
#      'red': 'красный'
#      }
with open('dict.json', 'r', encoding='utf-8') as fl:
    d = json.load(fl)
while True:
    word = input('Введите слово: ')
    if word in d:
        print(f'{word} - {d[word]} ')
    elif word == 'exit':
        break
    else:
        transl = input(f'введите перевод слова {word}: ')
        d[word] = transl

        with open('dict.json', 'w', encoding='utf-8') as fl:
            json.dump(d, fl)