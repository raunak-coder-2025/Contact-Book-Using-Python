import json
FILENAME = "contact book list.json"
def load_contacts():
    try:
        with open(FILENAME) as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def save_contacts(contacts):
    with open(FILENAME, "w") as f:
        json.dump(contacts, f, indent = 4)
def contact_book():
    contacts = load_contacts()
    print("\n____CONTACT BOOK MENU____")
    print("Choices:")
    print("1.Add a new contact")
    print("2.View all contact")
    print("3.Search for a contact's detail")
    print("4.Delete a contact")
    print("5. Update any contact's detail")
    print("6.exit")
    print("-"*40)
    while True:
        
        choice = input("enter your choice(1-6): ")
        print("")
        if choice == "1":
            name = input("enter the contact name: ").lower()
            number = input("enter the contact number: ").lower()
            email = input("enter email address: ").lower()
            if any(contact["name"] == name for contact in contacts):
                print("This contact name already exists! Try a different name.")
                print("-" * 40)
            else:
                contacts.append({"name": name, "number": number, "email": email})
                print("Contact added successfully!")
                print("-" * 40)
                save_contacts(contacts)
        elif choice == "2":
            if not contacts:
                print("no contact found")
                print("-"*40)
            else:
                for i, t in enumerate(contacts, start = 1):
                    print(f"{i}. Name: {t['name']}, Phone no: {t['number']}, Email: {t['email']}")
                    print("-"*40)
                
        elif choice == "3":
            search = input("enter contact name to see the contact detail: ").lower()
            found = False
            for t in contacts:
                if t['name'].lower() == search.lower():
                    print(f"Found: {t['name']} - {t['number']} - {t['email']}")
                    print("-"*40)
                    found = True
                    break
            if not found:
                print("contact not found")
                print("-"*40)
        elif choice == "4":
            delete = input("enter contact name to delete the contact: ").lower()
            found = False
            for t in contacts:
                if t['name'] == delete:
                    contacts.remove(t)
                    found = True
                    print("contact deleted succesfully!")
                    print("-"*40)
                    break
            save_contacts(contacts)
            if not found:
                print("contact not found")
                print("-"*40)
        elif choice == "5":
            update_contact = input("Enter contact name: ").lower()
            found = False
            for i in contacts:
                if i['name'] == update_contact:
                    print("What you want to change?\nChoices:\n1. Name\n2. Phone number\n3. Email")
                    choose = input("Enter choice which you want to change: ")
                    if choose == "1":
                        new_name = input("Enter new name: ").lower()
                        if any(contact["name"] == new_name for contact in contacts):
                            print("This name already exists! Choose a different name.")
                            print("-" * 40)
                        else:
                            i['name'] = new_name
                            print("Name updated successfully!")
                            print("-" * 40)
                    elif choose == "2":
                        new_number = input("Enter new phone number: ").lower()
                        i['number'] = new_number
                        print("Phone number updated succesfully!")
                        print("-"*40)
                    elif choose == "3":
                        new_email = input("Enter new email address: ").lower()
                        i['email'] = new_email
                        print("Email updated succesfully!")
                        print("-"*40)
                    else:
                        print("Invalid choice\n please choose a valid option(1-3)")
                        print("-"*40)
                    found = True
                    break
            save_contacts(contacts)
            if not found:
                print("Contact not found!")
                print("-"*40)
        elif choice == "6":
                print("Thank You for using contact book!")
                print("-"*40)
                break
        else:
            print("Invalid choice\nPlease enter a valid choice(1-6)")
            print("-"*40)
        
contact_book()
