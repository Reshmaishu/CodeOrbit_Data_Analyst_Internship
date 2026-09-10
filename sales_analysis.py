import pandas as pd

# Load the sales dataset
df = pd.read_csv("sales_data.csv")

# Calculate Sales Amount
df["Sales_Amount"] = df["Quantity"] * df["Unit_Price"]

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------
# 1. Basic Dataset Information
# -----------------------------
print("===== SALES DATA ANALYSIS =====")
print("\nDataset:")
print(df)

print("\nTotal Number of Orders:", len(df))

# -----------------------------
# 2. Total Sales
# -----------------------------
total_sales = df["Sales_Amount"].sum()
print("\nTotal Sales: ₹", total_sales)

# -----------------------------
# 3. Average Order Value
# -----------------------------
average_order_value = df["Sales_Amount"].mean()
print("Average Order Value: ₹", round(average_order_value, 2))

# -----------------------------
# 4. Top Products
# -----------------------------
top_products = (
    df.groupby("Product")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== TOP PRODUCTS =====")
print(top_products)

# -----------------------------
# 5. Category-wise Sales
# -----------------------------
category_sales = (
    df.groupby("Category")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== CATEGORY-WISE SALES =====")
print(category_sales)

# -----------------------------
# 6. Region-wise Sales
# -----------------------------
region_sales = (
    df.groupby("Region")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== REGION-WISE SALES =====")
print(region_sales)

# -----------------------------
# 7. Time-period Analysis
# -----------------------------
monthly_sales = (
    df.groupby(df["Date"].dt.to_period("M"))["Sales_Amount"]
    .sum()
)

print("\n===== MONTHLY SALES =====")
print(monthly_sales)

# -----------------------------
# 8. Save Analysis to Excel
# -----------------------------
with pd.ExcelWriter("sales_analysis.xlsx") as writer:
    df.to_excel(writer, sheet_name="Sales Data", index=False)
    top_products.to_frame("Total Sales").to_excel(
        writer, sheet_name="Top Products"
    )
    category_sales.to_frame("Total Sales").to_excel(
        writer, sheet_name="Category Sales"
    )
    region_sales.to_frame("Total Sales").to_excel(
        writer, sheet_name="Region Sales"
    )
    monthly_sales.to_frame("Total Sales").to_excel(
        writer, sheet_name="Monthly Sales"
    )

print("\nAnalysis completed successfully!")
print("Excel report saved as sales_analysis.xlsx")
