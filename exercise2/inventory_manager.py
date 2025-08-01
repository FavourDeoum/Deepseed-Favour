def format_currency(value):
    return f"${value:.2f}"

# Initial Inventory
inventory = {
    "apple": {"price": 0.5, "stock": 10, "category": "fruit"},
    "bread": {"price": 1.2, "stock": 4, "category": "bakery"},
    "milk": {"price": 2.5, "stock": 2, "category": "dairy"}
}


def show_menu():
    print("\n=== SMART INVENTORY MANAGER ===")
    print("1. Add new item")
    print("2. Update stock (add/remove)")
    print("3. Search items by category")
    print("4. Check low stock items (≤5 units)")
    print("5. Calculate total inventory value")
    print("6. Exit ")

def main_loop():

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            update_stock()
        elif choice == "3":
            search_by_category()
        elif choice == "4":
            check_low_stock()
        elif choice == "5":
            calculate_total_inventory()
        elif choice == "6":
            print("Exiting inventory manager.")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


def add_item():
    name= input("Enter item name: ").strip().lower()
    if name in inventory:
        print("Stock already exist. use update option instead")
        return
    try:
        price = float(input("Enter item price: "))
        stock = int(input("Enter item stock quantity: "))
        category = input("Enter item category: ").strip().lower()
        inventory[name] = {"price": price, "stock": stock, "category": category}
        print(f"{name.title()} added successfully.")
    except ValueError:
        print("Invalid input. Price must be a number and stock must be an integer.")


def update_stock():
    name = input("Enter item name to update: ").strip().lower()
    if name not in inventory:
        print("Item not found.")
        return
    try:
        change = int(input("Enter quantity to add (+) or remove (-): "))
        new_stock = inventory[name]["stock"] + change
        new_stocks = inventory[name]["stock"] - change
        if new_stock < 0:
            print("Stock cannot be negative.")
        else:
            inventory[name]["stock"] = new_stock
            inventory[name]["stock"] = new_stocks
            print(f"Stock updated. New stock: {inventory[name]['stock']}")
    except ValueError:
        print("Invalid input. Please enter an integer.")


def search_by_category():
    category = input("Enter category to search: ").strip().lower()
    found = False
    for item, details in inventory.items():
        if details["category"] == category:
            print(f"{item.title()} - ({format_currency(details['price'])}) - {details['stock']} in stock")
            found = True
    if not found:
        print("No items found in this category.")


def check_low_stock():
    print("Low stock items (≤5 units):")
    low = False
    for item, details in inventory.items():
        if details["stock"] <= 5:
            print(f"{item.title()} - {details['stock']} units")
            low = True
    if not low:
        print("No low stock items.")


def calculate_total_inventory():
    total = sum(details["price"] * details["stock"] for details in inventory.values())
    print(f"Total inventory value: {format_currency(total)}")


main_loop()
