from collections import UserDict
import datetime
from datetime import datetime, date, timedelta
from functools import wraps
from os import name



class Field:


    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    

class Name(Field):

        
    def __init__(self, value):
        self.value = value


class Phone(Field):

    
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10 : 
            raise ValueError("Phone number must be at least 10 digits and contain only numbers.")
        else:
            self.value = value

class Birthday(Field):


    def __init__(self, value):
        try:    
            self.value = datetime.strptime(value, "%d.%m.%Y").date()        
            #day, month, year = map(int, value.split('.'))            
            #self.value = datetime.date(year, month, day)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")           


class Record:

    
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.birthday = None


    def add_phone(self, phone):
        self.phones.append(Phone(phone))


    def add_email(self, email): 
        self.emails.append(email)    

    def add_birthday(self, birthday): 
        self.birthday = Birthday(birthday)           


    def edit_phone(self, old_phone, new_phone):
        if self.find_phone(old_phone) is None:
            raise ValueError("Old phone number not found.")
        else:
            self.add_phone(new_phone)            
            self.remove_phone(old_phone)

    def edit_email(self, old_email, new_email):  
        if self.find_email(old_email):
            self.add_email(new_email)
            self.remove_email(old_email) 


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
   

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, emails: {self.emails}, \
            birthday: {self.birthday.value if self.birthday else 'N/A'}"
    

class AddressBook(UserDict): 


    def add_record(self, Record):        
        self.data[Record.name.value] = Record


    def delete(self, name):
        if name in self.data:
            del self.data[name]


    def find(self, name):  
        return self.data.get(name) 
    
    
    def date_to_string(date):  #переформотування дата рядока в рядок 
        return date.strftime("%Y.%m.%d")


    
    def find_next_weekday(birthday, weekday): #присвоєння дати на понед якщо випадає вихідн день 
        days_ahead = weekday - birthday.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return birthday + timedelta(days=days_ahead)


    
    def adjust_for_weekend(birthday): #встановлення birthday чи є вихідн день 
        birthday_next_weekday = find_next_weekday(birthday, 0)
        if birthday.weekday() >= 5:
            return birthday_next_weekday
        else :
            return birthday


    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []    
        today = datetime.date.today() 

        for data in self.data.values():
            birthday_this_year = data.birthday.value.replace(year = today.year)   
            birtday_weekday = adjust_for_weekend(birthday_this_year)
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year = today.year + 1)                

            if 0 <= int((birthday_this_year - today).days) <= days:
                birthday_this_year = birtday_weekday          
                congratulation_date_str = date_to_string(birthday_this_year)
                data.birthday.value = congratulation_date_str
                upcoming_birthdays.append({"name": data.name.value, "birthday": data.birthday.value})
        return upcoming_birthdays
    
    
    def __str__(self):
        return f"Record name: {'; '.join(self.data.keys())},\
{'; '.join(f'contact name: {str(Record.name.value)},\
phones: {", ".join(str(phone.value) for phone in Record.phones )},\
emails: {str(Record.emails)}, birthday: {Record.birthday.value if Record.birthday else "N/A"}' for Record in self.data.values())}" 
<<<<<<< Updated upstream
  
=======
    
>>>>>>> Stashed changes

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "This contact does not exist."
        except IndexError:
            return "Invalid input. Please provide the required information."
        except AttributeError:
            return "Invalid input. Please provide the required information."
    return inner 
  

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    name, phone = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
<<<<<<< Updated upstream
        if phone:
            record.add_phone(phone)    
=======
    if phone:
        record.add_phone(phone)    
>>>>>>> Stashed changes
    return message


@input_error
def change_contact(args, book):
<<<<<<< Updated upstream
    name, phone, emails, birthdays = args     
    book[name] = phone
    if emails:
        book[name] = emails
    if birthdays:
        book[name] = birthdays    
    return "Contact updated."   
    
=======
    name, phone = args     
    record = book.find(name)
    if record is None:   
        return "Contact not found."  
    else:
        record.edit_phone(record.phones[0].value, phone) 
    return "Contact updated."
        
>>>>>>> Stashed changes

@input_error
def show_phone(args, book):
    name = args[0]        
<<<<<<< Updated upstream
    return f"{name}: {book[name]}"     
       
=======
    return f"{name}: {book[name]}"      
>>>>>>> Stashed changes
        
@input_error        
def show_all_contacts(book): 
    if book:
        return str(book)
    else:
        return "No contacts found." 
    

@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    record.add_birthday(birthday)
    return "Birthday added."
<<<<<<< Updated upstream
   
=======

>>>>>>> Stashed changes

@input_error
def show_birthday(args, book):
    name = args[0]
    return f"{name}: {book[name]}"
<<<<<<< Updated upstream
    
=======

>>>>>>> Stashed changes

@input_error
def birthdays(args, book):
    days = int(args[0]) 
    upcoming_birthdays = book.get_upcoming_birthdays(book, days)
    if upcoming_birthdays:
<<<<<<< Updated upstream
        for birthday in upcoming_birthdays:
            return(f"Name: {birthday['name']}, Congratulation date: {birthday['congratulation_date']}")
=======
        return upcoming_birthdays
>>>>>>> Stashed changes
    else:
        return("No upcoming birthdays.")


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all_contacts(book))
        elif command == "add-birthday": 
            print(add_birthday(args, book)) 
        elif command == "show-birthday":
            print(show_birthday(args, book)) 
        elif command == "birthdays":
            print(birthdays(args, book)) 
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()







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
# print(book)  # Виведення всіх записів у книзі після видалення Jane
