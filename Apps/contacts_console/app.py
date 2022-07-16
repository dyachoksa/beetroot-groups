# before running: pip install rich
from rich.console import Console
from rich.prompt import Prompt

from contacts import (
    add_contact,
    remove_contact_by_email, 
    get_contacts, 
    search_contact
)
from contacts.formatters import get_console_table

print("Welcome to the Contacts v1.1!")

console = Console()

while True:
    print("""
a - add a contact
d - remove the contact
p - print list of contacts
s - search for a contact
q - quit from app
    """)

    action = Prompt.ask("Choise your action")

    if action == "q":
        print("Thank you! See you soon!")
        break

    elif action == "a":
        name = input("Enter a name: ")
        email = input("Enter an email: ")
        phone = input("Enter a phone: ")
        address = input("Enter an address (optional): ")
        notes = input("Enter the notes (optional): ")

        add_contact(
            name, email, phone, address=address, notes=notes
        )

        print("Contact added successfully!")

    elif action == "r":
        email = Prompt.ask("Enter email of the contact to remove")

        ok = remove_contact_by_email(email)

        if ok:
            print("Contact removed successfully!")
        else:
            print("No contact found with email {}".format(email))
    
    elif action == "s":
        value = Prompt.ask("Search")

        contact = search_contact(value)

        if contact is None:
            print("Contact not found...")
            continue

        table = get_console_table(contact, "Search results")

        console.print(table)


    elif action == "p":
        contacts = get_contacts()

        table = get_console_table(contacts)
        
        console.print(table)

    else:
        print("Unknown action!")
