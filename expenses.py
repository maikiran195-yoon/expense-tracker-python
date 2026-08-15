expenses = []
try:
    file = open("expenses.txt", "r")
    expenses = file.readlines()

    cleaned_expenses = []

    for line in expenses:
        line = line.strip()
        cleaned_expenses.append(line)

    expenses = cleaned_expenses

    file.close()

except FileNotFoundError:
    print("No saved expenses found.")
while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Edit expense")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        expense = input("Enter expense name: ")
        amount = input("Enter expense amount: ")
        file = open("expense.txt","a")
        expenses.append(expense + " - ₹" + amount)
        file.write(expense +"- ₹" + amount)
        file.close()
        print(expenses)
        print("Expense added successfully!")

    elif choice == "2":
        print("\nYour Expenses:")
        total=0
        for i,expense in enumerate(expenses,start=1):
            print(i,".",expense)
            total = total + int(expense.split("₹")[1])
        print("Total Expenses: ₹", total)
    elif choice == "3":
         print("\nyour Expenses:")
         for i, expense in enumerate(expenses,start=1):
             print(i,".",expense)
         delete=int(input("enter expense number to delete :"))
         expenses.pop(delete-1)
         print ("expense deleted successsfully!")
    elif choice == "4":
        print("\nyour expenses")

        for i, expense in enumerate(expenses,start=1):
            print(i,".",expense)
        edit=int(input("enter expense number to edit:"))
        new_expense = input("Enter new expense name: ")
        new_amount = input("Enter new expense amount: ")
        expenses[edit - 1] = new_expense + " - ₹" + new_amount
        1
        print("Expense updated successfully!")

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")