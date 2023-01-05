class UserDict():
    data = {}

class AddressBook(UserDict):


    def add_record(self, name, phone):
        self.name = name
        self.phone = phone
        print(f"Test: {self.phone}")
        self.data[self.name] = self.phone

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
        
        return self.name

    def Phone(self):
        
        return self.phone



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