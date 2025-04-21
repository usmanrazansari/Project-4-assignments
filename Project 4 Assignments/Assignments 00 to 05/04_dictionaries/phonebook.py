def phonebook():
    contacts = {}
    
    while True:
        print("\nPhonebook Menu:")
        print("1. Add contact")
        print("2. Look up contact")
        print("3. Delete contact")
        print("4. List all contacts")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            name = input("Enter contact name: ")
            number = input("Enter phone number: ")
            contacts[name] = number
            print(f"Contact {name} added successfully!")
            
        elif choice == "2":
            name = input("Enter contact name to look up: ")
            if name in contacts:
                print(f"{name}'s number is {contacts[name]}")
            else:
                print("Contact not found")
                
        elif choice == "3":
            name = input("Enter contact name to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"Contact {name} deleted successfully!")
            else:
                print("Contact not found")
                
        elif choice == "4":
            if not contacts:
                print("Phonebook is empty")
            else:
                print("\nAll contacts:")
                for name, number in sorted(contacts.items()):
                    print(f"{name}: {number}")
                    
        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    phonebook() 