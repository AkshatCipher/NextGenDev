contacts = []
n=1
def add_contact(name, phone, email, address):
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print("Contact",name, "added successfully!")

def view_contacts():
    if not contacts:
        print("Contact list is empty.")
    else:
        print("List of Contacts:")
        for index, contact in enumerate(contacts, start=1):
            print(index,". Name:",contact['name'], ", Phone:",contact['phone'])

def update_contact(name, phone, email, address):
    updated = False
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contact['phone'] = phone
            contact['email'] = email
            contact['address'] = address
            print("Contact ",name," updated successfully!")
            updated = True
    if not updated:
        print("Contact ",name," not found.")


def search_contact(query):
    found = False
    if query.isdigit():
        for contact in contacts:
            if query == contact['phone']:
                print("Name:", contact['name'], ", Phone:", contact['phone'], ", Email:", contact['email'], ", Address:", contact['address'])
                found = True
            if not found:
                print("No contacts found with the phone number: ",query,".")

    else:
        for contact in contacts:
            if query.lower() == contact['name'].lower():
                print("Name:", contact['name'], ", Phone:", contact['phone'], ", Email:", contact['email'], ", Address:", contact['address'])
                found = True
        if not found:
            print("No contacts found with the name: ", query)

def delete_contact(name):
    deleted = False
    for contact in contacts[:]:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print("Contact ",name," deleted successfully!")
            deleted = True
    if not deleted:
        print("Contact ",name," not found.")
while n!=0:
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        add_contact(name, phone, email, address)

    elif choice == '2':
        view_contacts()

    elif choice == '3':
        query = input("Enter name or phone number to search: ")
        search_contact(query)

    elif choice == '4':
        name = input("Enter name of contact to update: ")
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        update_contact(name, phone, email, address)

    elif choice == '5':
        name = input("Enter name of contact to delete: ")
        delete_contact(name)

    elif choice == '6':
        print("Exiting Contact Book.")
        n=0
        
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
