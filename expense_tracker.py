import os

FILE_NAME = "expenses.txt"

# Add expense
def add_expense():
    category = input("Enter category (Food, Travel, etc): ")
    amount = input("Enter amount: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{category},{amount}\n")

    print("Expense added successfully!\n")


# View expenses
def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.\n")
        return

    total = 0
    print("\n--- Expense List ---")

    with open(FILE_NAME, "r") as file:
        for line in file:
            category, amount = line.strip().split(",")
            print(f"{category}: ₹{amount}")
            total += float(amount)

    print(f"\nTotal खर्च: ₹{total}\n")


# Main menu
def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


# Run program
main()