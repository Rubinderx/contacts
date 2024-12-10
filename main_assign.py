class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = [
            Contact("Alice", "1234567890", "alice@email.com"),
            Contact("Bob", "9876543210", "bob@email.com")
        ]

    def add_contact(self, name, phone_number, email):

        new_contact = Contact(name, phone_number, email)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added successfully.")

    def display_all_contacts(self):
        if self.contacts:
            print("All Contacts:")

            for contact in self.contacts:
                print(f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\n")
        else:
            print("No contacts found.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"\nContact Found:\nName: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}")
            
            else:
                print(f"\nSorry, no contact found with the name '{name}'.")

    #Missing UPDATE contact function

    #Missing DELETE cointact functions

def main():
    contact_book = ContactBook()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add New Contact")
        print("2. Display All Contacts")
        print("3. Search Contacts")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone_number, email)
        elif choice == "2":
            contact_book.display_all_contacts()
        elif choice == "3":
            search_name = input("Who are you searching for: ")
            contact_book.search_contact(search_name)
        elif choice == "0":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            #Needs code here to check incorrect user choice 
            print("")

if __name__ == "__main__":
    main()
