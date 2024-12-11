from colorama import Fore, Style

# class for individual contacts
class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

# manages contacts
class ContactBook:
    def __init__(self):
        self.contacts = [
            Contact("alice", "1234567890", "alice@email.com"),
            Contact("bob", "9876543210", "bob@email.com")
        ]

    # add function
    def add_contact(self, name, phone_number, email):
        new_contact = Contact(name, phone_number, email) # creates a new contact object
        self.contacts.append(new_contact) # adds contact to list
        print(Fore.GREEN + f"Contact '{name}' added successfully.")

    # display function
    def display_all_contacts(self):
        if self.contacts: # checks if there are any contacts
            print(Fore.BLUE + "All Contacts:")

            for contact in self.contacts: # goes through all contacts
                print(Fore.YELLOW + f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\n")
        else:
            print(Fore.RED + "No contacts found.") # if no contacts exist

    # search function
    def search_contact(self, name):
        for contact in self.contacts: # goes through all contacts
            if contact.name.lower() == name:
                print(Fore.GREEN + f"\nContact Found:\nName: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}")
                return contact # chatgpt help
            print(Fore.RED + f"\nSorry, no contact found with the name '{name}'.")
            return None # chatgpt help, also had a else statement here as well that it helped with

    # update fuction
    def update_contact(self, name):
        contact = self.search_contact(name) # search function attaches to variable
        if contact:
            print(Fore.BLUE + "What would you like to update")
            print(Fore.YELLOW + "1. Name")
            print(Fore.YELLOW + "2. Phone Number")
            print(Fore.YELLOW + "3. Email")
            
            while True: # start of loop until valid input
                choice = input(Fore.YELLOW + "Enter your choice: ").strip().lower()
                if choice == "1": # update name
                    new_name = input(Fore.YELLOW + "Enter new name: ").strip().lower()
                    if new_name:
                        contact.name = new_name
                        print(Fore.GREEN + f"Contact's name updated - {new_name}-")
                    else:
                        print(Fore.RED + "Please enter a name.")
                    break

                elif choice == "2": # update number
                    new_phone_number = input(Fore.YELLOW + "Enter new phone number: ").strip().lower()
                    if new_phone_number:
                        contact.phone_number = new_phone_number
                        print(Fore.GREEN + f"Contact's phone number updated - {new_phone_number} -")
                    else:
                        print(Fore.RED + "Please enter a phone number.")
                    break

                elif choice == "3": # update email
                    new_email = input(Fore.YELLOW + "Enter new email: ").strip().lower()
                    if new_email:
                        contact.email = new_email
                        print(Fore.GREEN + f"Contact's email updated - {new_email} -")
                    else:
                        print(Fore.RED + "Please enter an email.")
                    break
                else:
                    print(Fore.RED + "Please enter 1, 2 or 3.") # end of loop until valid input

    # delete function
    def delete_contact(self, name):
        contact = self.search_contact(name) # search function attaches to variable
        if contact:
            self.contacts.remove(contact) # removes contact
            print(Fore.GREEN + f"Contact - {name} - has been deleted.")

# main function to start the program
def main():
    contact_book = ContactBook() # attaches class to variable

    while True: # main menu loop
        print(Fore.BLUE + "\n--- Contact Book Menu ---")
        print(Fore.YELLOW + "1. Add New Contact")
        print(Fore.YELLOW + "2. Display All Contacts")
        print(Fore.YELLOW + "3. Search Contacts")
        print(Fore.YELLOW + "4. Update Contacts")
        print(Fore.YELLOW + "5. Delete Contact")
        print(Fore.YELLOW + "0. Exit")

        choice = input(Fore.YELLOW + "Enter your choice: ") # user input

        if choice == "1": # adds contacts
            name = input(Fore.YELLOW + "Enter name: ").strip().lower()
            phone_number = input(Fore.YELLOW + "Enter phone number: ")
            email = input(Fore.YELLOW + "Enter email: ").strip().lower()
            contact_book.add_contact(name, phone_number, email)

        elif choice == "2": # displays contacts
            contact_book.display_all_contacts()

        elif choice == "3": # search's contacts
            search_name = input(Fore.YELLOW + "Who are you searching for: ").strip().lower()
            contact_book.search_contact(search_name)

        elif choice == "4": # update's contacts
            update_name = input(Fore.YELLOW + "Which contact are you trying to update: ").strip()
            contact_book.update_contact(update_name)

        elif choice == "5": # delete's contacts
            delete_name = input(Fore.YELLOW + "Which contact are you trying to delete: ").strip()
            contact_book.delete_contact(delete_name)

        elif choice == "0": # ends program
            print(Fore.GREEN + "Exiting Contact Book. Goodbye!")
            break

        else: # invalid input
            print(Fore.RED + "Please enter a number between 0 and 5.")

if __name__ == "__main__":
    main()
