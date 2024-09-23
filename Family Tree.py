family_info = {}

def add_person(name, age, children=None):
    if name in family_info:
        print(f"The name: {name} already exists.")
    else:
        if children is None:
            children = []
        family_info[name] = {'name': name, 'age': age, 'children': children}
        print(f"Person '{name}' has been added.")

def add_children(parent_name, children):
    if parent_name in family_info:
        family_info[parent_name]['children'].extend(children)
        print(f"'{children}' have been added to '{parent_name}'")
    else:
        print(f"{parent_name} does not exist.")

def update_age(name, age):
    if name in family_info:
        family_info[name]['age'] = age
        print(f"Age of {name} has been updated to {age}.")
    else:
        print(f"Person {name} doesn't exist in the system.")

def display_family():
    if family_info:
        print("Family Tree:")
        for name, info in family_info.items():
            children_names = ', '.join(str(child) for child in info['children']) if info['children'] else 'None'
            print(f"Name: {info['name']}, Age: {info['age']}, Children: {children_names}")
    else:
        print("The family tree is empty.")
        
# Test the functions
add_person("John", 50)
add_person("Alice", 45)
add_children("John", ["Mike", "Emma"])
add_children("Alice", ["Mike", "Emma"])
add_person("Mike", 20)
update_age("John", 51)
display_family()

# Trying to add a person who already exists
add_person("John", 51)

# Trying to add children to a non-existent person
add_children("Charlie", ["Sam"])

# Trying to update age for a non-existent person
update_age("Charlie", 30)
