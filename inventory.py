# Inventory system using dictionary
inventory = {
    "Books": 10,
    "Novels": 20,
    "Pencils": 15,
    "Rubbers" :45,
    "Sets" :105
}

def display_inventory():
    print("\nCurrent Inventory:")
    if not inventory:
        print("Inventory is empty.")
    else:
        for item, quantity in inventory.items():
            print(f"{item}: {quantity} in stock")
#defining functions for updating the inventory list
def add_item():
    item = input("Enter item name to add: ").capitalize()
    if item in inventory:
        print(f"{item} already exists.")
    else:
        quantity = int(input(f"Enter quantity for {item}: "))
        inventory[item] = quantity
        print(f"{item} added to inventory.")
def update_item():
    item = input("Enter item name to update: ").capitalize()
    
    if item in inventory:
        print(f"Current quantity of {item}: {inventory[item]}")
        
        # Asking a user if they want to change the name as they update an item record
        rename = input("Do you want to change the item name? (yes/no): ").strip().lower()
        
        if rename == "yes":
            new_name = input("Enter the new item name: ").capitalize()
        else:
            new_name = item  # Keep the same name
        
        # Ask for the new quantity 
        quantity = int(input(f"Enter new quantity for {new_name}: "))
        
        # Delete old item if name changed
        if new_name != item:
            del inventory[item]
        
        # Add/update the item
        inventory[new_name] = quantity
        print(f"{item} updated to {new_name} with a quantity of {quantity}!!")
    
    else:
        print(f"{item} does not exist in inventory.")
def delete_item():
    item = input("Enter item name to delete: ").capitalize()
    if item in inventory:
        del inventory[item]
        print(f"{item} removed from inventory.")
    else:
        print(f"{item} not found.")
# Main loop
while True:
    print("\n<--- Inventory Menu --->")
    print("1. Display Inventory")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit System")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        display_inventory()
    elif choice == '2':
        add_item()
    elif choice == '3':
        update_item()
    elif choice == '4':
        delete_item()
    elif choice == '5':
        print("Exiting inventory system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
