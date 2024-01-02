contacts = {}

def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")

    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print(f"\nContact '{name}' added successfully.")

def view_contact_list():
    if not contacts:
        print("\nContact list is empty.")
    else:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            print("-" * 20)

def search_contact():
    search_term = input("\nEnter the name or phone number to search: ")
    found_contacts = []

    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['Phone']:
            found_contacts.append((name, details))

    if not found_contacts:
        print("No matching contacts found.")
    else:
        print("\nMatching Contacts:")
        for name, details in found_contacts:
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            print("-" * 20)

def update_contact():
    name = input("\nEnter the name of the contact to update: ")

    if name in contacts:
        print(f"\nCurrent details for '{name}':")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}")
        print(f"Address: {contacts[name]['Address']}")
        print("\nEnter the new details:")
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")
        address = input("Enter the new address: ")

        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        print(f"\nContact '{name}' updated successfully.")
    else:
        print(f"Contact with name '{name}' not found.")

def delete_contact():
    name = input("\nEnter the name of the contact to delete: ")

    if name in contacts:
        del contacts[name]
        print(f"\nContact '{name}' deleted successfully.")
    else:
        print(f"Contact with name '{name}' not found.")

while True:
    print("\nContact Management System:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")

    try:
        choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contact_list()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()
    elif choice == 6:
        print("\nExiting the Contact Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

    input("Press Enter to continue...")
