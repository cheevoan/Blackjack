contact = {}

def add_contact():
    key = input("Add name: ").strip().title()
    value = input("Add phone: ").strip()
    if not key or not value.isdigit():
        print("Error: Invalid input, please try again!")
        return
    contact.setdefault(key[0], {})[key] = value
    print(f"Phone {key} added successfully!")


def display_contact():
    if not contact:
        print("No contact:")
        return
    print("All contacts:")
    for letter, names in sorted(contact.items()):
        print(f"{letter}:")
        for key, value in sorted(names.items()):
            print(f"  {key} : {value}")


def remove_contact():
    key = input("Enter the contact name to remove: ").strip().title()
    if not key:
        print("Name cannot be empty, please try again!")
        return
    first_letter = key[0]
    if contact.get(first_letter, {}).pop(key, None) is None:
        print(f"Contact \"{key}\" not found!")
    else:
        if not contact[first_letter]:
            del contact[first_letter]
        print(f"Contact \"{key}\" removed successfully!")


def update_contact():
    key = input("Enter the contact name to update: ").strip().title()
    if not key:
        print("Name cannot be empty, please try again!")
        return
    first_letter = key[0]
    if key not in contact.get(first_letter, {}):
        print(f"Contact \"{key}\" not found!")
        return
    new_value = input("Enter new phone: ").strip()
    if not new_value.isdigit():
        print("Phone can only contain numbers, please try again!")
    else:
        contact[first_letter][key] = new_value
        print(f"Contact \"{key}\" updated successfully!")


def menu():
    while True:
        print("Option: \n1. Display contacts \n2. Add new contact \n3. Remove contact \n4. Update contact \n5. Exit program")
        user_input = input("Enter option: ").strip()
        match user_input:
            case "1": display_contact()
            case "2": add_contact()
            case "3": remove_contact()
            case "4": update_contact()
            case "5":
                print("Exiting program.")
                break
            case _: print("Invalid option, please try again!")


if __name__ == "__main__":
    menu()