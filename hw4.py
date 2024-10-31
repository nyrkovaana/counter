documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}


def p(number):
    for doc in documents:
        if doc['number'] == number:
            return doc['name']
    return "Not found"


def s(number):
    for key, value in directories.items():
        if number in value:
            return key
    return "Not found"


command = input("Введите команду: ")

while command != "q":
    data = input("Введите номер документа: ")

    if command == "p":
        print("Владелец документа: ", p(data))

    if command == "s":
        print("Документ хранится на полке: ", s(data))

    command = input("Введите команду: ")