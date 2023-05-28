import argparse
import decorators, address_book
from constants import (
    COMANDS_WITHOUT_ARGUMENTS,
    COMANDS_WITH_ARGUMENTS
)
from commands import (
    add_contact,
    remove_phone,
    replace_phone,
    change_contact,
    show_contact,
    change_birthday,
    days_to_birthday,
    show_contacts_page,
    search_contact
)


def command_call(command: str, arguments: argparse):
    if command == 'add':
        result = add_contact(arguments.name, arguments.phone, arguments.birthday)
    elif command == 'change':
        if arguments.delete_phone:
            result = remove_phone(arguments.name, arguments.delete_phone)
        elif arguments.replace_phone:
            result = replace_phone(arguments.name, arguments.phone, arguments.replace_phone)
        elif arguments.phone and not arguments.replace_phone:
            result = change_contact(arguments.name, arguments.phone)
        elif arguments.birthday:
            result = change_birthday(arguments.name, arguments.birthday)
    elif command == 'show':
        if arguments.name and arguments.birthday == 'list':
            result = days_to_birthday(arguments.name)
        elif arguments.name:
            result = show_contact(arguments.name, 'name')
        elif arguments.phone:
            result = show_contact(arguments.phone, 'phone')
        elif arguments.search:
            result = search_contact(arguments.search)
        elif arguments.all == 'page':
            result = show_contacts_page()
    else:
        result = 'Wrong command! Try again'            
    return result

    

@decorators.input_error
def build_parser(arguments: str):
    parser = argparse.ArgumentParser(description="Contact book")
    parser.add_argument("-n", dest="name")
    parser.add_argument("-p", dest="phone")
    parser.add_argument("-r", dest="replace_phone")
    parser.add_argument("-d", dest="delete_phone")
    parser.add_argument("-b", dest="birthday")
    parser.add_argument("-a", dest="all")
    parser.add_argument("-s", dest="search")
    args = parser.parse_args(arguments.split())
    return args


def command_parser(user_input: str):
    command_elements = user_input.split(' ')
    if len(command_elements) < 2:
        arguments = None
        return command_elements[0], arguments
    else:
        arguments = user_input.split(' ', 1)[1]
        parsed_args = build_parser(arguments)
        return command_elements[0], parsed_args

def main():
    '''---------------------------
        add -n [name] (optional: -p [phone] -b [birthday]) - add new contact.
        change -n [name] -p [phone]- change existing contact.
        change -n [name] -d [phone]- remove existing phone.
        change -n [name] -b [birthday]- add birthday in format dd.mm.yyyy
        show -n [name] - show number or -p [phone] - show name.
        show -n -b list - show count days to the next birthday
        show -a page - show 5 contacts per page
        show -s - searches for matches in name and phones
        show_all - show all stored contacts and their numbers.
        To terminate the program, enter one of the following commands:
        good_bye
        close
        exit
        \n---------------------------'''
    
    address_book.contact_book
    while True:
        user_input = input('\nWait command #:').lower()
        command, arguments = command_parser(user_input)

        if command in COMANDS_WITHOUT_ARGUMENTS:
            result = COMANDS_WITHOUT_ARGUMENTS[command]()
            print(result)
            if result == 'Good bye!':
                break
        elif not arguments:
            print('Wrong command! Try again with arguments!')
        elif command in COMANDS_WITH_ARGUMENTS:
            print(command_call(command, arguments))

        else:
            print('Wrong command! Try again!')



if __name__ == '__main__':
    main()