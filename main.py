from expense import Expense
from manager import ExpenseManager
from datetime import date
from ai_model import predict_category

manager = ExpenseManager("data.csv")

while True:
    print("\n====== EXPENSE TRACKER (AI POWERED) ======")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Spending")
    print("4. Monthly Report")
    print("5. Category Report")
    print("6. Pie Chart")
    print("7. Bar Chart")
    print("8. Budget Check")
    print("9. Exit")

    choice = input("Enter choice: ")

    # ➕ ADD EXPENSE
    if choice == "1":
        amt = float(input("Enter amount: "))
        desc = input("Enter description: ")

        today = date.today()

        category = predict_category(desc)

        exp = Expense(amt, category, today, desc)
        manager.add_expense(exp)

        print(f"Expense Added ✅ | Category: {category}")

    elif choice == "2":
        manager.show_expenses()

    elif choice == "3":
        manager.total_spending()

    elif choice == "4":
        manager.monthly_report()

    elif choice == "5":
        manager.category_report()

    elif choice == "6":
        manager.pie_chart()

    elif choice == "7":
        manager.bar_chart()

    elif choice == "8":
        budget = float(input("Enter your monthly budget: "))
        manager.budget_check(budget)

    elif choice == "9":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice ❌")