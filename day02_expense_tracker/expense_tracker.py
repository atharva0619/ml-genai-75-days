expenses = []

def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        expenses.append({"amount": amount, "category": category})
        print("Expense added!\n")
    except ValueError:
        print("Please enter a valid number!\n")

def view_expenses():
    if not expenses:
        print("No expenses yet.\n")
        return
    
    print("\nAll Expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. ₹{exp['amount']} - {exp['category']}")
    print()

def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Spending: ₹{total}\n")

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")
    
    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice\n")
