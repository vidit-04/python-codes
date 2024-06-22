import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from the file."""
    if not os.path.isfile(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as file:
        contacts = json.load(file)
    return contacts

def save_contacts(contacts):
    """Save contacts to the file."""
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def display_contacts(contacts):
    """Display the list of contacts."""
    if not contacts:
        print("No contacts to display.")
    else:
        print("Your contact list:")
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def add_contact(contacts):
    """Add a new contact to the list."""
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"Contact '{name}' added.")

def update_contact(contacts):
    """Update an existing contact in the list."""
    display_contacts(contacts)
    contact_number = int(input("Enter the number of the contact to update: "))
    if 1 <= contact_number <= len(contacts):
        contact = contacts[contact_number - 1]
        print(f"Updating contact: {contact['name']}")
        name = input(f"Enter new name (or press enter to keep '{contact['name']}'): ")
        phone = input(f"Enter new phone number (or press enter to keep '{contact['phone']}'): ")
        email = input(f"Enter new email address (or press enter to keep '{contact['email']}'): ")
        if name:
            contact['name'] = name
        if phone:
            contact['phone'] = phone
        if email:
            contact['email'] = email
        print(f"Contact '{contact['name']}' updated.")
    else:
        print("Invalid contact number.")

def delete_contact(contacts):
    """Delete a contact from the list."""
    display_contacts(contacts)
    contact_number = int(input("Enter the number of the contact to delete: "))
    if 1 <= contact_number <= len(contacts):
        removed_contact = contacts.pop(contact_number - 1)
        print(f"Contact '{removed_contact['name']}' deleted.")
    else:
        print("Invalid contact number.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book Menu")
        print("1. View contacts")
        print("2. Add a contact")
        print("3. Update a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == '3':
            update_contact(contacts)
            save_contacts(contacts)
        elif choice == '4':
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == '5':
            print("Exiting the contact book application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
