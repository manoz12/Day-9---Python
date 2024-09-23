# Initialize dictionary to store item information
item_info = {}  # Corrected from `nitem_info`

# Function to add a new item with its quantity and price
def add_item(item_name, quantity, price):
    if item_name in item_info:
        print(f" The item '{item_name}' already exists.")
    else:
        item_info[item_name] = {'quantity': quantity, 'price': price}
        print(f"{item_name} is successfully added.")

# Function to update the quantity or price of an existing item
def update_item(item_name, quantity=None, price=None):
    if item_name in item_info:
        if quantity is not None:
            item_info[item_name]['quantity'] = quantity
        if price is not None:
            item_info[item_name]['price'] = price  # Corrected from item_name[item_name]['price']
        print(f" The information for {item_name} updated successfully.")
    else:
        print(f"The item: '{item_name}' doesn't exist.")

# Function to remove an item from the inventory
def remove_item(item_name):
    if item_name in item_info:
        del item_info[item_name]
        print(f"The item {item_name} has been deleted.")
    else:
        print(f"The item {item_name} not found.")

# Function to display all items with their quantity and price
def display_item():
    if item_info:
        print("Item Information:")
        for item_name, info in item_info.items():
            print(f"Item Name: '{item_name}', Quantity: {info['quantity']}, Price: {info['price']}")
    else:
        print("No items in Records.")

# Test the functions
add_item("Rice", 10, 530)
add_item("Dal", 2, 200)
display_item()

update_item("Rice", price=550)
display_item()

remove_item("Dal")
display_item()
