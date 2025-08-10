from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
	pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

        if len(value) != 10 or not value.isdigit():
            raise ValueError("Invalid phone number. Must contain exactly 10 digits.")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        old_phone_obj = Phone(old_phone)     # перевірка ValueError
        new_phone_obj = Phone(new_phone)     # перевірка ValueError
                         
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return

        raise ValueError("File not found.")
    
                
    def find_phone(self, phone):
        for p in self.phones:
            if phone in p.value:
                return Phone(phone)

        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, Record):
        self.data[Record.name.value] = Record

    def find(self, name):
        if name in self.data.keys():
            return self.data[name]
        else:
            return None
        
    def delete(self, name):
        del self.data[name]
         
    def __str__(self):
        return str(self.values)
    

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
    
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
