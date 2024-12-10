class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = [
            Contact("alice", "1234567890", "alice@email.com"),
            Contact("bob", "9876543210", "bob@email.com")
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
                return contact # chatgpt help
            else:
                print(f"\nSorry, no contact found with the name '{name}'.")
                return

    def update_contact(self, name):
        contact = self.search_contact(name)
        if contact:
            print("What would you like to update")
            print("1. Name")
            print("2. Phone Number")
            print("3. Email")
            
            while True:
                choice = input("Enter your choice: ").strip().lower()
                if choice == "1":
                    new_name = input("Enter new name: ")
                    if new_name:
                        contact.name = new_name
                        print(f"Contact's name updated - {new_name}-")
                    else:
                        print("Please enter a name.")
                    break

                elif choice == "2":
                    new_phone_number = input("Enter new phone number: ").strip().lower()
                    if new_phone_number:
                        contact.phone_number = new_phone_number
                        print(f"Contact's phone number updated - {new_phone_number} -")
                    else:
                        print("Please enter a phone number.")
                    break

                elif choice == "3":
                    new_email = input("Enter new email: ").strip().lower()
                    if new_email:
                        contact.email = new_email
                        print(f"Contact's email updated - {new_email} -")
                    else:
                        print("Please enter an email.")
                    break
                else:
                    print("Please enter 1, 2 or 3.")

    #Missing DELETE cointact functions

def main():
    contact_book = ContactBook()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add New Contact")
        print("2. Display All Contacts")
        print("3. Search Contacts")
        print("4. Update Contacts")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ").strip().lower()
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ").strip().lower()
            contact_book.add_contact(name, phone_number, email)
        elif choice == "2":
            contact_book.display_all_contacts()
        elif choice == "3":
            search_name = input("Who are you searching for: ").strip().lower()
            contact_book.search_contact(search_name)
        elif choice == "4":
            update_name = input("Which contact are you trying to update: ").strip().lower()
            contact_book.update_contact(update_name)
        elif choice == "0":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            #Needs code here to check incorrect user choice 
            print("")

if __name__ == "__main__":
    main()
