import pandas as pd

# ---------------------------------------------------------
# CODEORBIT TECH - DATA ANALYST INTERNSHIP
# TASK 1: DATA CLEANING
# ---------------------------------------------------------

# STEP 1: Create a small sample dataset with data problems
data = {
    "Customer_ID": ["C001", "C002", "C003", "C004", "C005", "C005", "C006"],
    "Name": ["John", " Alice ", "Rahul", "Priya", "David", "David", "Sara"],
    "Age": [25, 30, None, 28, 35, 35, None],
    "City": ["Hyderabad", "hyderabad", "Bangalore", " HYDERABAD ", "Mumbai", "Mumbai", "Bangalore"],
    "Purchase_Amount": [1500, 2200, 1800, None, 3500, 3500, 2500]
}

df = pd.DataFrame(data)

# Save the original dataset
df.to_csv("raw_data.csv", index=False)

print("ORIGINAL DATASET")
print(df)

# ---------------------------------------------------------
# STEP 2: Check for missing values
# ---------------------------------------------------------

print("\nMISSING VALUES BEFORE CLEANING")
print(df.isnull().sum())

# Fill missing Age values with the average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Purchase Amount values with 0
df["Purchase_Amount"] = df["Purchase_Amount"].fillna(0)

# ---------------------------------------------------------
# STEP 3: Remove duplicate records
# ---------------------------------------------------------

df = df.drop_duplicates()

# ---------------------------------------------------------
# STEP 4: Fix formatting issues
# ---------------------------------------------------------

# Remove extra spaces from Name
df["Name"] = df["Name"].str.strip()

# Standardize City names
df["City"] = df["City"].str.strip().str.title()

# ---------------------------------------------------------
# STEP 5: Format numerical columns
# ---------------------------------------------------------

df["Age"] = df["Age"].round(0).astype(int)

df["Purchase_Amount"] = df["Purchase_Amount"].round(2)

# ---------------------------------------------------------
# STEP 6: Check cleaned dataset
# ---------------------------------------------------------

print("\nCLEANED DATASET")
print(df)

print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

print("\nDUPLICATES AFTER CLEANING")
print(df.duplicated().sum())

# ---------------------------------------------------------
# STEP 7: Save cleaned dataset
# ---------------------------------------------------------

df.to_csv("cleaned_data.csv", index=False)

# Save an Excel version
df.to_excel("cleaned_data.xlsx", index=False)

# ---------------------------------------------------------
# STEP 8: Create cleaning documentation
# ---------------------------------------------------------

report = """
CODEORBIT TECH - TASK 1 DATA CLEANING REPORT

Dataset: Customer Purchase Sample Dataset

Cleaning Steps Applied:

1. Missing Values:
   - Missing Age values were replaced with the average age.
   - Missing Purchase Amount values were replaced with 0.

2. Duplicate Records:
   - Duplicate customer records were identified and removed.

3. Formatting Issues:
   - Extra spaces were removed from customer names.
   - City names were standardized using consistent capitalization.

4. Numerical Formatting:
   - Age values were rounded to whole numbers.
   - Purchase Amount values were rounded to two decimal places.

5. Output:
   - raw_data.csv contains the original dataset.
   - cleaned_data.csv contains the cleaned dataset.
   - cleaned_data.xlsx contains the cleaned dataset in Excel format.
"""

with open("cleaning_report.txt", "w") as file:
    file.write(report)

print("\nTask 1 data cleaning completed successfully!")
print("Files created:")
print("- raw_data.csv")
print("- cleaned_data.csv")
print("- cleaned_data.xlsx")
print("- cleaning_report.txt")