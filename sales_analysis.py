import pandas as pd

# Load the dataset
data = pd.read_csv("sales_data.csv")

# Display first 5 rows
print("First 5 rows of dataset:")
print(data.head())

print("\n-----------------------------")

# Total Sales
total_sales = data["Sales"].sum()
print("Total Sales:", total_sales)

# Total Profit
total_profit = data["Profit"].sum()
print("Total Profit:", total_profit)

# Average Sales
average_sales = data["Sales"].mean()
print("Average Sales:", average_sales)

# Highest Sale
highest_sale = data["Sales"].max()
print("Highest Sale:", highest_sale)

# sales by product bar chart
import matplotlib.pyplot as plt

print("\nCreating Bar Chart...")

# Group sales by product
product_sales = data.groupby("Product")["Sales"].sum()

# Create bar chart
product_sales.plot(kind="bar")

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()

# Monthly sales trend line chart

#add month column

print("\nCreating Monthly Sales Trend...")

# Convert Date to datetime
data["Date"] = pd.to_datetime(data["Date"])

# Extract Month
data["Month"] = data["Date"].dt.month

# create line chart / Time series analysis 
# Group sales by month
monthly_sales = data.groupby("Month")["Sales"].sum()

# Create line chart
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

# Export cleaned data for Power BI

data.to_csv("cleaned_sales_data.csv", index=False)

print("\nData exported successfully as cleaned_sales_data.csv")