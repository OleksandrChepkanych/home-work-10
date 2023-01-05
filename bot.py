def input_error(func):
    """Перевірка вводу"""
    def error_add(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("Input error. Try again")
        except ValueError:
            print("Input error. Try again")
        except IndexError:
            print("Input error. Try again")

    return error_add



def open_file(path):
    """Зчитання файлу"""
    contacts = {}
    with open(path, 'r', encoding="UTF8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            line_split = line.split(':')
            contacts[line_split[0]] = line_split[1].removesuffix('\n')
    return contacts

def close_file(path, contacts):
    """Закриття файлу"""
    with open(path, 'w', encoding="UTF8") as file:
        for name, number in contacts.items():
            file.write(f"{name}:{number}\n")


@input_error
def add(*args, **kwargs):
    name = args[0]
    phone = args[1]
    kwargs.get('contacts')[name] = phone
    return f'Contact {name} with {phone} add success'


def show_all(*args, **kwargs):
    contacts = kwargs.get('contacts')
    return '\n'.join([f'{name} : {phone}' for name, phone in contacts.items()])


def end_work(*args, **kwargs):
    return 'Goodbye'


COMMANDS = {add: ['add'],
            end_work: ['.', 'exit', 'bye'],
            show_all: ['show all', 'show']}

def parser_comand(command_line):
    for command, key_words in COMMANDS.items():
        for word in key_words:
            if command_line.startswith(word):
                return command, command_line.replace(word, '').strip().split(' ')
    return None, None

"""Основна функція. Безкінечний цикл """
def main():
    path = 'C:\Work Python\home-work-9\home-work-9\contact.txt'
    contacts = open_file(path)
    while True:
        command_line = input('Input comand: ')

        command, data = parser_comand(command_line)

        if command:
            print(command(*data, contacts=contacts))

        if command == end_work:
            break

if __name__ == '__main__':
# Виклик основної функції
    main()
