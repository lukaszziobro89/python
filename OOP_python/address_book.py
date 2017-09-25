menu_options = ('1,2,3,4,5,6'.split(','))
contacts = {}


class Contact(object):
    # Constructor
    def __init__(self, first_name, last_name, phone_number):
        if len(first_name) < 2:
            raise ValueError("First name must be at least 2 characters long.")

        if len(last_name) < 2:
            raise ValueError("Last name must be at least 2 characters long.")

        if len(phone_number) < 5 and phone_number[:].isdigit():
            raise ValueError("Phone number must contains only digits and have at least 5 numbers.")

        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number

    # Properties
    def first_name(self):
        return self._first_name

    def last_name(self):
        return self._last_name

    def phone_number(self):
        return self._phone_number

    def print_details(self):
        print("{} - {} - {}".format(self._first_name, self._last_name, self._phone_number))


option = 0
while True:
    print("-" * 31)
    option = input("Choose option:" + '\n'
                   "-------------------------------" + '\n'
                   '1. Add contact' + '\n'
                   '2. Print Address Book' + '\n'
                   '3. Delete contact' + '\n'
                   '4. Modify contact' + '\n'
                   '5. Search contact' + '\n'
                   '6. Quit' + '\n'
                   "-------------------------------" '\n>> ')
    if option == '6':
        break
    elif option == '1':
        print("You have choose option 1.")
    elif option == '2':
        print("")
    elif option == '3':
        print("")
    elif option == '4':
        print("")
    elif option == '5':
        print("")
    else:
        print("Unknown choice!")



