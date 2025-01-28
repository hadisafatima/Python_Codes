# This is a Basic Contact Book Program which adds, removes, lists and sorts the contacts

class ContactBook:
    def __init__(self):
        self.contacts = []




    def add_contacts(self, contact):
        name, number = contact
        if any(existing[1] == number for existing in self.contacts):
            print(f"'{number}' already exists in the Contact Book.")
        else:
            self.contacts.append(contact)
            print(f"Contact of '{name}' with number '{number}' added successfully.")




    def remove_contact(self, contact_number):
        if not self.contacts:
            print("Your Contact Book is empty.")
            return

        for existing in self.contacts:
            if contact_number == existing[1]:
                self.contacts.remove(existing)
                print(f"Contact with number '{contact_number}' removed successfully.")
                return

        print(f"'{contact_number}' does not exist in the Contact Book.")




    def view_contacts(self):
        if self.contacts:
            print("\nContacts in the Contact Book:")
            for i, contact in enumerate(self.contacts, start = 1):
                # this enumerate() iterates the iteratable object starting with the index 1
                print(f"{i}. {contact[0]} ({contact[1]})")
        else:
            print("Contact Book is empty.")





    def clear_contact_book(self):
        if not self.contacts:
            # this checks if the list is already empty or not if yes then there is no need to clear it if no then 
            # contact book is emptied
            print("Contact Book is already empty.")
        else:
            self.contacts.clear()
            print("All contacts cleared from the Contact Book.")





    def sort_contact_book(self):
        if self.contacts:
            self.contacts.sort(key = lambda x: x[0])  # Sort by name
            # in this "x" contains the elements of contacts list one by one and take their 0th index value i.e name 
            # of the contact and pass it to "key" variable, on the basis of which sorting is done. 
            print("Sorted Contact Book:")
            self.view_contacts()
        else:
            print("Contact Book is empty.")





contacts = ContactBook()

while input("\n\nDo you want to save a new contact? (yes/no): ").strip().lower() == "yes":
    name = input("Contact Name: ")
    number = input("Contact Number: ")
    if number.isdigit():
        contacts.add_contacts([name, number])
    else:
        print("Invalid number. Please enter digits only. ")

contacts.view_contacts()



# this "if" checks whether there are any contacts in contact book or not if yes program asks user if the user wants 
# to delete any, if there aren't any program won't ask 
if len(contacts.contacts) > 0 :
    while input("Do you want to remove any contact? (yes/no): ").strip().lower() == "yes" :
        contact_number = input("Provide the 'CONTACT NUMBER' to delete: ")

        while not contact_number.isdigit() :
            # this checks if the provided contact number is a digit or not, if not then user is asked to provide 
            # correct contact number
            contact_number = input("Invalid number. Please enter digits only. ")
        else :
            contacts.remove_contact(contact_number)
            contacts.view_contacts()
    

# this "if" checks if the contact book has more than one contacts, if yes it asks user whether user want to sort the contact book or not
if len(contacts.contacts) > 1 and input("\nDo you want to sort the Contact Book? (yes/no): ").strip().lower() == "yes":
    contacts.sort_contact_book()