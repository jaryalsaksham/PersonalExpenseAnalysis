import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load expense data
df = pd.read_csv("expenses.csv")

# Prepare data
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M").astype(str)

print("PERSONAL EXPENSE ANALYSIS")
print("-" * 35)
print("\nFirst five records:")
print(df.head())

# Basic summary
total_expenses = df["amount"].sum()
average_expense = df["amount"].mean()
average_daily_expense = df.groupby("date")["amount"].sum().mean()
category_totals = df.groupby("category")["amount"].sum().sort_values(ascending=False)
monthly_totals = df.groupby("month")["amount"].sum()

print(f"\nTotal expenses: Rs. {total_expenses:.2f}")
print(f"Average transaction amount: Rs. {average_expense:.2f}")
print(f"Average spending per day with a recorded expense: Rs. {average_daily_expense:.2f}")
print(f"Highest spending category: {category_totals.idxmax()} (Rs. {category_totals.max():.2f})")

print("\nExpenses by category:")
print(category_totals.to_string())

print("\nExpenses by month:")
print(monthly_totals.to_string())

print("\nExpenses by payment method:")
print(df.groupby("payment_method")["amount"].sum().sort_values(ascending=False).to_string())

# 1. Pie chart: expense share by category
plt.figure(figsize=(8, 6))
category_totals.plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.title("Share of Expenses by Category")
plt.ylabel("")
plt.tight_layout()
plt.savefig("category_pie_chart.png", dpi=150)
plt.show()

# 2. Bar chart: total expenses by category
plt.figure(figsize=(8, 5))
category_totals.plot(kind="bar")
plt.title("Total Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Amount (Rs.)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("category_bar_chart.png", dpi=150)
plt.show()

# 3. Line chart: monthly expenses
plt.figure(figsize=(8, 5))
monthly_totals.plot(kind="line", marker="o")
plt.title("Monthly Expense Trend")
plt.xlabel("Month")
plt.ylabel("Amount (Rs.)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("monthly_line_chart.png", dpi=150)
plt.show()
