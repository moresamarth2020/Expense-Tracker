# Store expenses in a list
expenses = []

# Add new expense
def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food, Travel, Bills, etc.): ")
    amount = float(input("Enter amount spent: "))
    note = input("Enter note/description: ")
    
    expense = {
        "Date": date,
        "Category": category,
        "Amount": amount,
        "Note": note
    }
    expenses.append(expense)
    print("✔ Expense added successfully!\n")

# View all expenses
def view_expenses():
    if not expenses:
        print("⚠ No expenses found!\n")
        return
    print("\n=== All Expenses ===")
    total = 0
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['Date']} | {e['Category']} | ₹{e['Amount']} | {e['Note']}")
        total += e['Amount']
    print(f"\n💰 Total Spent: ₹{total}\n")

# Search by category
def search_expense():
    cat = input("Enter category to search: ")
    found = [e for e in expenses if e['Category'].lower() == cat.lower()]
    if not found:
        print("⚠ No expenses found for this category!\n")
        return
    print(f"\n=== Expenses in {cat} ===")
    for e in found:
        print(f"{e['Date']} | ₹{e['Amount']} | {e['Note']}")

# Main menu
def menu():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search by Category")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_expense()
        elif choice == "4":
            print("Exiting... Bye 👋")
            break
        else:
            print("⚠ Invalid choice!\n")

# Run the system
menu()
