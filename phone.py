# -----------------------------
#     PHONE BOOK PROJECT
# -----------------------------

def is_valid_phone(number):
    """
    Validates a phone number:
    - Must be exactly 10 digits long
    - Must start with 6, 7, 8, or 9
    - Must contain digits only (no letters or symbols)
    """
    return number.isdigit() and len(number) == 10 and number[0] in '6789'


def display_menu():
    """
    Displays the main menu of the phone book application.
    """
    print("\n" + "-" * 30)
    print("     📞 PHONE BOOK MENU     ")
    print("-" * 30)
    print("1 : Add Contact")
    print("2 : Delete Contact")
    print("3 : Search Contact")
    print("4 : Display All Contacts")
    print("5 : Exit")
    print("-" * 30)


def add_contact(phone_book):
    """
    Adds a new contact to the phone book.
    Prompts the user for a name and a valid phone number.
    """
    name = input("Enter Name : ").strip()
    if not name:
        print("❌ Name cannot be empty.")
        return phone_book

    number = input("Enter Phone Number : ").strip()

    # Validate the phone number before adding
    if is_valid_phone(number):
        phone_book[name] = number
        print(f"✅ '{name}' has been added successfully.")
    else:
        print("❌ Invalid phone number! Must be 10 digits, start with 6/7/8/9, and contain only digits.")

    return phone_book


def delete_contact(phone_book):
    """
    Deletes an existing contact from the phone book.
    Prompts the user for the contact name.
    """
    name = input("Enter Name to Delete : ").strip()
    if name in phone_book:
        del phone_book[name]
        print(f"🗑️  '{name}' has been deleted from the phone book.")
    else:
        print(f"❌ '{name}' not found in the phone book.")
    return phone_book


def search_contact(phone_book):
    """
    Searches for a contact by name and displays the phone number if found.
    """
    name = input("Enter Name to Search : ").strip()
    if name in phone_book:
        print(f"🔍 '{name}' found with number: {phone_book[name]}")
    else:
        print(f"❌ '{name}' not found in the phone book.")


def display_contacts(phone_book):
    """
    Displays all the contacts in the phone book.
    """
    print("\n📋 CONTACT LIST")
    if not phone_book:
        print("⚠️  Phone book is empty.")
    else:
        for name, number in phone_book.items():
            print(f"• {name} : {number}")


# -----------------------------
#           MAIN
# -----------------------------

def main():
    """
    Main driver function of the phone book project.
    Contains the program loop and handles user choices.
    """
    phone_book = {}  # Empty dictionary to store contacts

    # Welcome Message
    print("=" * 40)
    print("      📱 SIMPLE PHONE BOOK PROJECT")
    print("=" * 40)

    # Infinite loop to keep the program running until user exits
    while True:
        display_menu()

        try:
            choice = int(input("Enter Your Choice (1-5): "))
        except ValueError:
            print("❌ Please enter a valid number (1-5).")
            continue

        # Match-case to handle different menu options
        match choice:
            case 1:
                phone_book = add_contact(phone_book)
            case 2:
                phone_book = delete_contact(phone_book)
            case 3:
                search_contact(phone_book)
            case 4:
                display_contacts(phone_book)
            case 5:
                print("\n📴 Exiting... Thank you for using the Phone Book!")
                break
            case _:
                print("❌ Invalid choice. Please select from 1 to 5.")


# Run the project only if this file is executed directly
if __name__ == "__main__":
    main()
