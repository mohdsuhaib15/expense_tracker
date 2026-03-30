import csv
from datetime import date
print("\nEXPENSE TRACKER\n")
file_name = "expenses.csv"
def addexpense():
    amount = float(input("Enter amount spent: ₹"))
    category = input("Enter category (food/travel/study/misc): ").lower()
    today = date.today()
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, category, amount])
    print("Expense added.\n")
def showsummary():
    totals = {}
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[1]
                amount = float(row[2])
                if category in totals:
                    totals[category] += amount
                else:
                    totals[category] = amount
        print("\nExpense Summary\n")
        grand_total = 0
        for category, amount in totals.items():
            print(f"{category.capitalize()} → ₹{round(amount,2)}")
            grand_total += amount
        print("\nTotal Spent → ₹", round(grand_total,2))
    except FileNotFoundError:
        print("No expenses recorded yet.")
while True:
    print("\n1. Add Expense")
    print("2. Show Summary")
    print("3. Exit")
    choice = input("Choose option: ")
    if choice == "1":
        addexpense()

    elif choice == "2":
        showsummary()

    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("Invalid choice")
