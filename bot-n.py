class UserDict():
    contacts = {}
    path = 'C:\Work Python\home-work-10\home-work-10\contact.txt'
    with open(path, 'r', encoding="UTF8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            line_split = line.split(':')
            contacts[line_split[0]] = line_split[1].removesuffix('\n')

class AddressBook(UserDict):
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def add_record(self):
        print(f"Test: {self.phone}")
        self.contacts[self.name] = self.phone

class Field():
    pass

class Name(Field):
    def __init__(self, name):
        self.name = str(name)

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

class Record():
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def Name(self):
        
        return str(self.name)

    def Phone(self):
        
        return str(self.phone)



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