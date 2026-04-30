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

    def pie_chart(self):
        df = pd.read_csv(self.file)
        data = df.groupby("category")["amount"].sum()

        plt.pie(data, labels=data.index, autopct="%1.1f%%")
        plt.title("Expense Distribution")
        plt.show()

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