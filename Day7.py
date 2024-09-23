# Create a dictionary representing a simple phone book where the keys are names and the values are phone numbers. Add, update, and delete entries from the phone book.

# # Initialize an empty dictionary for the phone book
# phone_book = {}

# # Function to add a new contact
# def add_contact(name, number):
#     if name in phone_book:
#         print(f"{name} already exists. Use update_contact to update the number.")
#     else:
#         phone_book[name] = number
#         print(f"Contact {name} added with number {number}.")

# # Function to update an existing contact
# def update_contact(name, number):
#     if name in phone_book:
#         phone_book[name] = number
#         print(f"Contact {name} updated with new number {number}.")
#     else:
#         print(f"Contact {name} does not exist. Use add_contact to add the contact.")

# # Function to delete a contact
# def delete_contact(name):
#     if name in phone_book:
#         del phone_book[name]
#         print(f"Contact {name} deleted.")
#     else:
#         print(f"Contact {name} does not exist in the phone book.")

# # Function to display all contacts
# def display_contacts():
#     if phone_book:
#         print("Phone Book:")
#         for name, number in phone_book.items():
#             print(f"Name: {name}, Number: {number}")
#     else:
#         print("The phone book is empty.")

# # Example usage
# add_contact("Alice", "1234567890")
# add_contact("Bob", "0987654321")
# display_contacts()

# update_contact("Alice", "1111111111")
# delete_contact("Bob")
# display_contacts()

# # Trying to update a non-existent contact
# update_contact("Charlie", "2222222222")

# # Trying to delete a non-existent contact
# delete_contact("Charlie")

# Write a program that takes a paragraph of text as input and returns a dictionary where the keys are words and values are their frequencies.
# def word_frequencies(paragraph):
#     paragraph = paragraph.lower()
#     for char in "-./,\n":
#         paragraph = paragraph.replace(char, " ")
#     words = paragraph.split()
#     frequencies_dict = {}
#     for word in words:
#         if word in frequencies_dict:
#             frequencies_dict[word]+=1
#         else:
#             frequencies_dict[word] =1
#     return frequencies_dict

# # Take input from the user
# paragraph_input = input("Enter a paragraph of text:\n")

# # Get the word frequencies
# frequencies = word_frequencies(paragraph_input)

# # Display the word frequency dictionary
# print("Word Frequencies in the Paragraph:")
# for word, freq in frequencies.items():
#     print(f"'{word}': {freq}")

# Create a nested dictionary to store information about multiple people (name, age, hobbies). Write functions to add a new person, update an existing person's information, and delete a person.
people_info ={}
def add_person(name, age, hobbies):
    if name in people_info:
        print(f"person '{name}' already exist. Use update option to update the information")
    else:
        people_info[name] = {'age':age, 'hobbies': hobbies}
        print(f"Person '{name}'is successfully added")

def update_person(name, age= None,  hobbies= None):
    if name in people_info:
        if age is not None:
            people_info[name]['age']= age
        if hobbies is not None:
            people_info[name]['hobbies']= hobbies
        print(f"Information for '{name}' updated successfully.")
    else:
        print(f"Person '{name}' does not exist. Use add_person to add the person")  

def delete_person(name):
    if name in people_info:
        del people_info[name]
        print(f"The person '{name}' is successfully deleted.")
    else:
        print(f"Person '{name}' doesnot exist")
def display_person():
    if people_info:
        print("People Information")
        for name,info in people_info.items():
            print(f"Name:'{name}', Age: '{info['age']}', hobbies: {','.join(info['hobbies'])}")
    else:
        print("No people in records.")
add_person("Alice", 30, ["Reading", "Hiking"])
add_person("Bob", 25, ["Swimming", "Gaming"])
display_person()

update_person("Alice", hobbies=["Cooking", "Traveling"])
delete_person("Bob")
display_person()

# Trying to update a non-existent person
update_person("Charlie", age=22)

# Trying to delete a non-existent person
delete_person("Charlie")
        