import pandas as pd
import matplotlib.pyplot as plt

class ExpenseManager:
    def __init__(self, file):
        self.file = file

    def add_expense(self, expense):
        df = pd.read_csv(self.file)

        new_data = {
            "amount": expense.amount,
            "category": expense.category,
            "date": expense.date,
            "description": expense.description
        }

        df = pd.concat([df, pd.DataFrame([new_data])])
        df.to_csv(self.file, index=False)

    def show_expenses(self):
        df = pd.read_csv(self.file)
        print(df)

    def total_spending(self):
        df = pd.read_csv(self.file)
        print("Total Spending:", df["amount"].sum())

    def monthly_report(self):
        df = pd.read_csv(self.file)

        df["date"] = pd.to_datetime(df["date"])
        df["month"] = df["date"].dt.to_period("M")

        report = df.groupby("month")["amount"].sum()

        print("\n📊 Monthly Expense Report")
        print(report)

    def category_report(self):
        df = pd.read_csv(self.file)

        report = df.groupby("category")["amount"].sum()

        print("\n📊 Category-wise Spending")
        print(report)

    # 📊 PIE CHART
    def pie_chart(self):
        df = pd.read_csv(self.file)

        data = df.groupby("category")["amount"].sum()

        plt.pie(data, labels=data.index, autopct="%1.1f%%")
        plt.title("Expense Distribution")
        plt.show()

    # 📈 BAR CHART
    def bar_chart(self):
        df = pd.read_csv(self.file)

        df["date"] = pd.to_datetime(df["date"])
        df["month"] = df["date"].dt.to_period("M")

        data = df.groupby("month")["amount"].sum()

        data.plot(kind="bar")

        plt.title("Monthly Spending Trend")
        plt.xlabel("Month")
        plt.ylabel("Amount")
        plt.xticks(rotation=45)
        plt.show()

    # 💰 BUDGET SYSTEM
    def budget_check(self, budget):
        df = pd.read_csv(self.file)

        total = df["amount"].sum()

        print("\n💰 Budget Report")
        print("Budget:", budget)
        print("Spent:", total)

        if total > budget:
            print("⚠️ ALERT: You have exceeded your budget!")
        else:
            print("✅ You are within budget")