
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

os.makedirs("figures", exist_ok=True)
tips = sns.load_dataset("tips")   # public built-in dataset (BSD license)

# Visualization 1: tip vs total bill
fig, ax = plt.subplots(figsize=(7, 5))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", ax=ax)
ax.set_title("Tip vs Total Bill by Meal Time")
plt.tight_layout()
plt.savefig("figures/viz1_tip_vs_bill.png", dpi=150)
plt.close()

# Visualization 2: tip distribution by day
fig, ax = plt.subplots(figsize=(7, 5))
sns.boxplot(data=tips, x="day", y="tip", ax=ax)
ax.set_title("Tip Distribution by Day of Week")
plt.tight_layout()
plt.savefig("figures/viz2_tip_by_day.png", dpi=150)
plt.close()

# Simple regression
X, y = tips[["total_bill", "size"]], tips["tip"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)
print("Test R^2:", round(r2_score(y_test, model.predict(X_test)), 3))
print("Coefficients:", dict(zip(X.columns, model.coef_.round(3))))