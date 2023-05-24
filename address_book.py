import os.path
import classes


def load_contact_book():
    contact_book = classes.AddressBook()
    if os.path.exists('Address_Book.bin'):
        contact_book.load_address_book()
    return contact_book


contact_book = load_contact_book() 