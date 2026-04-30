from flask import Flask, render_template, request, redirect
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import os

from expense import Expense
from manager import ExpenseManager
from ai_model import predict_category

app = Flask(__name__, template_folder="templates")
manager = ExpenseManager("data.csv")


# 🏠 HOME
@app.route("/")
def home():
    return render_template("index.html")


# ➕ ADD
@app.route("/add", methods=["POST"])
def add():
    amount = float(request.form["amount"])
    desc = request.form["description"]

    category = predict_category(desc)
    today = date.today()

    exp = Expense(amount, category, today, desc)
    manager.add_expense(exp)

    return redirect("/")


# 📄 SHOW
@app.route("/show")
def show():
    df = pd.read_csv("data.csv")
    table = df.to_html(classes="table", index=False)
    return render_template("show.html", table=table)


# 📊 REPORT
@app.route("/report")
def report():
    df = pd.read_csv("data.csv")

    total = df["amount"].sum()
    category = df.groupby("category")["amount"].sum().reset_index()

    table = category.to_html(classes="table", index=False)

    return render_template("report.html", table=table, total=total)


# 📅 MONTHLY
@app.route("/monthly")
def monthly():
    df = pd.read_csv("data.csv")

    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")

    report = df.groupby("month")["amount"].sum().reset_index()
    table = report.to_html(classes="table", index=False)

    return render_template("monthly.html", table=table)


# 📊 CHARTS
@app.route("/charts")
def charts():
    df = pd.read_csv("data.csv")

    if df.empty:
        return "No data available"

    category = df.groupby("category")["amount"].sum()

    if not os.path.exists("static"):
        os.makedirs("static")

    # PIE
    plt.figure()
    category.plot.pie(autopct="%1.1f%%")
    plt.title("Expense Distribution")
    plt.ylabel("")
    plt.savefig("static/pie.png")
    plt.close()

    # BAR
    plt.figure()
    category.plot(kind="bar")
    plt.title("Category-wise Spending")
    plt.savefig("static/bar.png")
    plt.close()

    return render_template("charts.html")


# 💰 BUDGET
@app.route("/budget", methods=["GET", "POST"])
def budget():
    if request.method == "POST":
        budget_value = float(request.form["budget"])

        df = pd.read_csv("data.csv")
        total = df["amount"].sum()

        status = "Within Budget ✅" if total <= budget_value else "Over Budget ⚠️"

        return render_template("budget.html",
                               total=total,
                               budget=budget_value,
                               status=status)

    return render_template("budget.html")


# ▶ RUN
if __name__ == "__main__":
    app.run(debug=True)