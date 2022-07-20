import uuid
import json
import os.path

filename = "contacts.json"

# Contact should contain name, email, phone, address (optional) and notes (optional)
contacts = []
# contacts = [
#     {
#         "id": "441cbeea-b83f-46d0-924e-2069379d8102",
#         "name": 'Janice Thomas', 
#         "email": 'janice.thomas@example.com', 
#         "phone": '(272) 569-4415', 
#         "address": '2745 Thornridge Cir', 
#         "notes": None
#     },
#     {
#         "id": "2b3432ac-9417-4778-9aaa-dbfa8dc039c3",
#         "name": 'Cassandra Burton', 
#         "email": 'cassandra.burton@example.com', 
#         "phone": '(629) 326-8652', 
#         "address": None, 
#     },
# ]

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)

with open(file_path, "r") as f:
    contacts = json.load(f)


def get_contacts():
    return contacts


def search_contact(value):
    """Search contact by name, email or phone number"""
    if value is None or len(value) == 0:
        raise ValueError("Value can't be empty")

    value = value.lower()

    contacts = get_contacts()

    for contact in contacts:
        contact_name = contact["name"].lower()
        contact_email = contact["email"].lower()
        contact_phone = contact["phone"].lower()

        if contact_name.find(value) != -1 \
            or contact_email.find(value) != -1 \
            or value == contact_phone:
            return contact
    
    return None


def add_contact(name, email, phone, address=None, notes=None):
    if name is None or email is None or phone is None:
        raise ValueError("Name, email and phone are required")

    address = address if len(address) > 0 else None
    notes = notes if len(notes) > 0 else None

    contact = {
        "id": str(uuid.uuid4()),
        "name": name, 
        "email": email, 
        "phone": phone, 
        "address": address, 
        "notes": notes
    }

    contacts = get_contacts()

    contacts.append(contact)

    with open(file_path, "w") as f:
        json.dump(contacts, f, indent=2)


def remove_contact_by_email(email):
    if email is None or len(email) == 0:
        raise ValueError("Email can't be blank")

    contacts = get_contacts()
    
    for contact in contacts:
        if email.lower() == contact["email"].lower():
            contacts.remove(contact)

            with open(file_path, "w") as f:
                data = json.dumps(contacts, indent=2)
                f.write(data)
                # or
                # json.dump(contacts, f)

            return True

    return False
