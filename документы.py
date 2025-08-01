document = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "1006", "name": "Jhone Bom"}
]
# Перечень полок, на которых находятся документы хранится в следующем виде:


directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006', '1006'],
    '3': []
}
"""
    Задача №1
Необходимо реализовать пользовательские команды, которые будут
 выполнять следующие функции:

p – people – команда, которая спросит номер документа и выведет
имя человека, которому он принадлежит;
s – shelf – команда, которая спросит номер документа и выведет
 номер полки, на которой он находится;
Правильно обработайте ситуации, когда пользователь будет вводить
 несуществующий документ.
l– list – команда, которая выведет список всех документов в формате
passport “2207 876234” “Василий Гупкин”;
a – add – команда, которая добавит новый документ в каталог и
 в перечень полок, спросив его номер, тип, имя владельца и номер
 полки, на котором он будет храниться. Корректно обработайте
  ситуацию, когда пользователь будет пытаться добавить документ
   на несуществующую полку.
d– delete – команда, которая спросит номер документа и удалит
 полностью документ из каталога и его номер из перечня полок.
  Предусмотрите сценарий, когда пользователь вводит несуществующий
  документ;
m – move – команда, которая спросит номер документа и целевую
полку и переместит его с текущей полки на целевую. Корректно
обработайте кейсы, когда пользователь пытается переместить
несуществующий документ или переместить документ на несуществующую
полку;
as – add shelf – команда, которая спросит номер новой полки
 и добавит ее в перечень. Предусмотрите случай, когда
 пользователь добавляет полку, которая уже существует.;
 """


def people():
    """Поиск персоны по номеру документа."""
    print(people.__doc__)
    numb = input('Введите номер документа: ')
    for item in document:
        if item['number'] == numb:
            print(f'Номер документа "{numb}" принадлежит {item.get("name")}')
            return
    print(f'Нет человека с номером документа "543"')


def shelf():
    """Место хранения документа"""
    print(shelf.__doc__)
    numb = input('Введите номер документа: ')
    for k, v in directories.items():
        if numb in v:
            print(f'Документ № {numb} находится на {k} полке.')
            return
    print(f'Документ с номером {numb} в архиве не найден.')


def list():
    """Листинг документов."""
    print(list.__doc__)
    max_numb = max(document, key=lambda x: len(x.get('number')))
    # print(max_numb)
    mx = len(max_numb.get('number'))
    for i in document:
        long = " " * (mx - len(i["number"]))
        print(f'{i["type"]:9} "{i["number"]}" {long} "{i["name"]}"')


def add():
    """Добавление документа."""
    print(add.__doc__)
    d = {}
    d['type'] = input("Тип документа: ")
    d['number'] = input("Номер документа: ")
    d['name'] = input("Владелец документа: ")
    number_shelf = input("Номер полки: ")
    while number_shelf not in directories:
        number_shelf = input("введите правильный номер полки: ")
    document.append(d)
    directories[number_shelf].append(d['number'])
    print(f'Документ с номером {number_shelf} добавлен!')


def delete():
    """Удаление документа."""
    print(delete.__doc__)
    numb = input('Введите номер документа: ')
    for k, item in enumerate(document):
        if item['number'] == numb:
            for doc_numbs in directories.values():
                if numb in doc_numbs:
                    doc_numbs.remove(numb)
                    document.pop(k)
                    break
            else:
                print(f'Нет документа на полках ')
            return

    print(f'Нет человека с номером документа {numb}')


def move():
    """Перемещение документа."""
    print(move.__doc__)
    numb = input('Введите номер документа: ')
    for n_doc in directories.values():
        if numb in n_doc:
            n_shelf = input('Введите номер целевой полки: ')
            try:
                directories[n_shelf].append(numb)
                n_doc.remove(numb)
            except Exception:
                print(f'Нет полки с номером {n_doc}'


    print(f'Документ {numb} на полках отсутствует!')




commands = '''    Оглавлениеl
Поиск персоны по номеру документа - p;
Место хранения документа          - s;
Листинг документов                - l;
Добавление документа              - a;   
Удаление документа                - d;
> '''
while True:
    com = input(commands)
    match com.lower():
        case 'p':
            people()
        case 's':
            shelf()
        case 'l':
            list()
        case 'a':
            add()
        case 'd':
            delete()
        case 'exit':
            break
    print()
    print('-------------------------------------')
    print()
