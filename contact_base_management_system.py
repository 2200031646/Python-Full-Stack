#Contact Base Management System
class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}"
class ContactBook:
    def __init__(self):
        self.contacts = {}
    #Add Contact
    def add_contact(self, contact):
        if contact.name in self.contacts:
            print("Contact already exists.")
        else:
            self.contacts[contact.name] = contact
            print("Contact added successfully.")
    #Delete Contact
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")
    #Update Contact
    def update_contact(self, name):
        if name in self.contacts:
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")

            if len(phone_number) == 10 and phone_number.isdigit():
                if email.endswith("@gmail.com"):
                    self.contacts[name].phone_number = phone_number
                    self.contacts[name].email = email
                    print("Contact updated successfully.")
                else:
                    print("Invalid email. Please enter a Gmail address.")
            else:
                print("Invalid phone number. Please enter exactly 10 digits.")
        else:
            print("Contact not found.")
    #List Contacts
    def list_contacts(self):
        if len(self.contacts) == 0:
            print("No contacts found.")
        else:
            print("\n--- Contact List ---")

            for contact in self.contacts.values():
                print(contact)
    #Find Contact
    def find_contact(self, name):
        if name in self.contacts:
            print("\n--- Contact Found ---")
            print(self.contacts[name])
        else:
            print("Contact not found.")

#Main Application
contact_book = ContactBook()
while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. List Contacts")
    print("4. Delete Contact")
    print("5. Find Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        if len(phone_number) == 10 and phone_number.isdigit():
            email = input("Enter email: ")
            if email.endswith("@gmail.com"):
                contact = Contact(name, phone_number, email)
                contact_book.add_contact(contact)
            else:
                print("Invalid email. Please enter a Gmail address.")
        else:
            print("Invalid phone number. Please enter exactly 10 digits.")
    elif choice == "2":
        name = input("Enter name to update: ")
        contact_book.update_contact(name)
    elif choice == "3":
        contact_book.list_contacts()
    elif choice == "4":
        name = input("Enter name to delete: ")
        contact_book.delete_contact(name)
    elif choice == "5":
        name = input("Enter name to find: ")
        contact_book.find_contact(name)
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")


