options = ("""\
(1). View All Contacts (2). View Contact (3). Add Contact 
(4). Update Contact. (5): Remove Contact. (6): Exit
""")


contacts = {
    "Steve": "823-111-2384",
    "Kim": "823-843-2435",
}


steve_number = contacts["Steve"]
kim_number = contacts["Kim"]


#################################################


def view_all_contacts():
    if len(contacts) == 0:
        print("Your contacts are empty!")
        return

    for name, number in contacts.items():
        print(f"{name}'s phone number: {number}\n")


def view_contact():
    contact_name = input("\nEnter the name of the contact you'd like to view: ")
    print(contact_name)
    if contact_name in contacts:
        print(f"\nContact's Name: {contact_name}. Contacts Number: {contacts[contact_name]}\n") 

    else:

        print("\nContact does not exist.\n")
        

def add_contact():
    name = input("\nEnter the contact's name: ")
    number = input("Enter the contact's number: ")


    if name in contacts:
        print("That is already in your contacts!")

    else:

        contacts[name] = number
        print(f"\nAdded {name} to your contacts\n")


def update_contact():
    contact_name = input("\nContacts Name: ")

    if contact_name not in contacts:
        print("Contact does not exist.")

    else:

        print(f"\nEditing {contact_name}'s Number.")
        contact_number = input("\nContacts Number: ")

        contacts[contact_name] = contact_number
        print(f"\nSuccessfully Updated {contact_name}'s Number!\n")


def remove_contact():
    contact_name = input("\nContacts Name: ")
    if contact_name.strip().lower() == "*": 
        del contacts["Steve"]
        del contacts["Kim"]

    elif contact_name not in contacts:
        print("\nContact does not exist.\n")

    else:
        del contacts[contact_name]



########################## END FUNCTION DEFINITIONS ######################


while True:
    print(options)
    choice = int(input("Select an option: "))

    if choice == 1:
        view_all_contacts()

    elif choice == 2:
        view_contact()

    elif choice == 3:
        add_contact()

    elif choice == 4:
        update_contact()

    elif choice == 5:
        remove_contact()

    elif choice == 6:
        break

    else:
        print(f"{choice} is not a valid option")