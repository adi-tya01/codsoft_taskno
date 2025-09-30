# Contact Book Application in Python

def display_menu():
    print("\n====== CONTACT BOOK MENU ======")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("================================")

def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found!")
    else:
        print("\nContact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact(contacts):
    keyword = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break
    if not found:
        print("No contact found with that detail.")

def update_contact(contacts):
    view_contacts(contacts)
    if contacts:
        try:
            index = int(input("Enter contact number to update: ")) - 1
            if 0 <= index < len(contacts):
                print("\nEnter new details (leave blank to keep old value):")
                new_name = input(f"Name ({contacts[index]['name']}): ") or contacts[index]['name']
                new_phone = input(f"Phone ({contacts[index]['phone']}): ") or contacts[index]['phone']
                new_email = input(f"Email ({contacts[index]['email']}): ") or contacts[index]['email']
                new_address = input(f"Address ({contacts[index]['address']}): ") or contacts[index]['address']

                contacts[index] = {
                    "name": new_name,
                    "phone": new_phone,
                    "email": new_email,
                    "address": new_address
                }
                print("Contact updated successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number!")

def delete_contact(contacts):
    view_contacts(contacts)
    if contacts:
        try:
            index = int(input("Enter contact number to delete: ")) - 1
            if 0 <= index < len(contacts):
                removed = contacts.pop(index)
                print(f"Contact '{removed['name']}' deleted successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number!")

def main():
    contacts = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()