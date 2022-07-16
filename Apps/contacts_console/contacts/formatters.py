from rich.table import Table


def get_console_table(contacts, title="Contacts"):
    table = Table(title=title)

    table.add_column("Name", style="cyan")
    table.add_column("Email", style="cyan")
    table.add_column("Phone", style="magenta")
    table.add_column("Address")
    table.add_column("Notes")

    if type(contacts) != list:
        contacts = [contacts]

    for contact in contacts:
        table.add_row(
            contact["name"],
            contact["email"],
            contact["phone"],
            contact["address"] or "-",
            contact.get("notes", "-") or "-"
        )

    return table
