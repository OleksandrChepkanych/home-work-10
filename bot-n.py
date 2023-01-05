from collections import UserDict

class Field:
    def __init__(self, value) -> None:
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    pass

class Record():
    contacts = {}
    path = 'C:\Work Python\home-work-10\home-work-10\contact.txt'
    with open(path, 'r', encoding="UTF8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            line_split = line.split(':')
            contacts[line_split[0]] = line_split[1].removesuffix('\n')

    def __init__(self, name, phone=None):
        self.name = name
        if phone:
            self.phones = [phone]
        else:
            self.phones = []
    
    def Name(self):
        if self.name not in self.contacts:
            self.contacts[self.name] = ""
    
    def Phone(self):
        if self.name not in self.contacts:
            self.contacts[self.name] = self.phones

class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record
   


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    
    print('All Ok)')