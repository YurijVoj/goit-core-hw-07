from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу    
    def __init__(self, value):
        self.value = value


class Phone(Field):
     # реалізація класу
    def __init__(self, value):
        if not value.isdigit() or len(value) < 10: 
            raise ValueError("Phone number must be at least 10 digits and contain only numbers.")
        else:
            self.value = value

class Record:


    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.emails = []


    def add_phone(self, phone):
        self.phones.append(Phone(phone))


    def add_email(self, email): 
        self.emails.append(email)    


    def edit_phone(self, old_phone, new_phone):
        if self.find_phone(old_phone):
            self.remove_phone(old_phone)
            self.add_phone(new_phone)


    def edit_email(self, old_email, new_email):  
        if old_email in self.emails:
            self.emails.remove(old_email)
            self.emails.append(new_email)  

    def remove_email(self, email):
        if email in self.emails:
            self.emails.remove(email)        


    def remove_phone(self, phone):
        phone = self.find_phone(phone)
        if phone:
            self.phones.remove(phone)


    def find_email(self, email):
        for e in self.emails:
            if e == email:
                return e
        return None        


    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, emails: {'; '.join(self.emails)}"

class AddressBook(UserDict):
    # реалізація класу

    def add_record(self, Record):        
        self.data[Record.name.value] = Record


    def delete(self, name):
        if name in self.data:
            del self.data[name]


    def find(self, name):  
        return self.data.get(name)  
    
    def __str__(self):
        return f"Record name: {'; '.join(self.data.keys())}, contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, emails: {'; '.join(self.emails)}"

# book = AddressBook()

# # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")

# # Додавання запису John до адресної книги
# book.add_record(john_record)

# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# # Виведення всіх записів у книзі
     
# print(book)

    # # Знаходження та редагування телефону для John
    # john = book.find("John")
    # john.edit_phone("1234567890", "1112223333")

    # print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # # Пошук конкретного телефону у записі John
    # found_phone = john.find_phone("5555555555")
    # print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # # Видалення запису Jane
    # book.delete("Jane")
