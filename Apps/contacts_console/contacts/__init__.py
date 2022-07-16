import uuid

# Contact should contain name, email, phone, address (optional) and notes (optional)
contacts = [
    {
        "id": "441cbeea-b83f-46d0-924e-2069379d8102",
        "name": 'Janice Thomas', 
        "email": 'janice.thomas@example.com', 
        "phone": '(272) 569-4415', 
        "address": '2745 Thornridge Cir', 
        "notes": None
    },
    {
        "id": "2b3432ac-9417-4778-9aaa-dbfa8dc039c3",
        "name": 'Cassandra Burton', 
        "email": 'cassandra.burton@example.com', 
        "phone": '(629) 326-8652', 
        "address": None, 
    },
]


def get_contacts():
    return contacts


def search_contact(value):
    """Search contact by name, email or phone number"""
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


def remove_contact_by_email(email):
    contacts = get_contacts()
    
    for contact in contacts:
        if email.lower() == contact["email"].lower():
            contacts.remove(contact)
            return True

    return False
