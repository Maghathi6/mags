"""import pandas as pd

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")"""

"""print(df.isnull().sum())

# Fill missing values if any
df["Age"] = df["Age"].fillna(df["Age"].mean())

print("Missing values handled")""
"""print("Before:", len(df))

df = df.drop_duplicates()

print("After:", len(df))"""
"""df["Gender"] = df["Gender"].replace("male","Male")
df["Gender"] = df["Gender"].replace("MALE","Male")

df["Gender"] = df["Gender"].replace("female","Female")
df["Gender"] = df["Gender"].replace("FEMALE","Female")

print(df["Gender"].unique())
df["Department"] = df["Department"].replace("sales","Sales")

df["Department"] = df["Department"].replace(
    "human resources",
    "Human Resources"
)

print(df["Department"].unique())
df.info()
df["Age"] = df["Age"].astype(int)

df["MonthlyIncome"] = df["MonthlyIncome"].astype(float)

df.info()
Q1 = df["MonthlyIncome"].quantile(0.25)

Q3 = df["MonthlyIncome"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR

upper = Q3 + 1.5 * IQR

print("Lower Bound =", lower)

print("Upper Bound =", upper)

Q1 = df["MonthlyIncome"].quantile(0.25)

Q3 = df["MonthlyIncome"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR

upper = Q3 + 1.5 * IQR

df = df[(df["MonthlyIncome"] >= lower) &
        (df["MonthlyIncome"] <= upper)]

print(df.shape)
df.to_csv("cleaned_employee.csv", index=False)

print("Dataset Saved")
before = len(df)

df = df.drop_duplicates()

after = len(df)

print("Before =", before)

print("After =", after)

print("Removed =", before - after)
      
print("Data Cleaning Summary")
print("1. Missing values identified and handled")
print("2. Duplicate records removed")
print("3. Gender values standardized")
print("4. Department values standardized")
print("5. Data types verified and corrected")
print("6. Salary outliers removed using IQR")
print("7. Cleaned dataset saved")"""
"""import pandas as pd

df = pd.read_csv("dirty_cafe_sales.csv")"""

"""
print("\nDataset Information:")
df.info()

print("\nShape of Dataset:")
print(df.shape)"""
"""print(df.isnull().sum())
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors="coerce")
df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors="coerce")

# Fill missing values
df["Item"] = df["Item"].fillna("Unknown")

df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())

df["Price Per Unit"] = df["Price Per Unit"].fillna(
    df["Price Per Unit"].mean()
)

print("Missing values handled")"""
"""print("Duplicate Records =", df.duplicated().sum())
before = len(df)

df = df.drop_duplicates()

after = len(df)

print("Duplicates Removed =", before - after)"""
"""df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

df["Price Per Unit"] = pd.to_numeric(
    df["Price Per Unit"],
    errors="coerce"
)

invalid = df[(df["Quantity"] <= 0) |
             (df["Price Per Unit"] <= 0)]

print(invalid)
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

df["Price Per Unit"] = pd.to_numeric(
    df["Price Per Unit"],
    errors="coerce"
)

before = len(df)

df = df[(df["Quantity"] > 0) &
        (df["Price Per Unit"] > 0)]

after = len(df)

print("Invalid Transactions Removed =", before - after)"""
"""df["Transaction Date"] = pd.to_datetime(
    df["Transaction Date"],
    errors="coerce"
)

print(df["Transaction Date"])
df["Item"] = df["Item"].str.strip()

df["Item"] = df["Item"].str.title()

print(df["Item"].head())
df["Location"] = df["Location"].str.strip()

df["Location"] = df["Location"].str.title()

print(df["Location"].head())"""
"""missing_removed = df.isnull().sum().sum()

duplicate_removed = df.duplicated().sum()

print("Missing Values =", missing_removed)

print("Duplicate Records =", duplicate_removed)

print("Invalid Transactions = Check Quantity and Price Per Unit")"""
"""import pandas as pd

# Load dataset
df = pd.read_csv("dirty_cafe_sales.csv")

# Convert numeric columns
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors="coerce")

# -----------------------------
# Missing Values Removed
# -----------------------------

missing_before = df.isnull().sum().sum()

df["Item"] = df["Item"].fillna("Unknown")
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())
df["Price Per Unit"] = df["Price Per Unit"].fillna(df["Price Per Unit"].mean())

missing_after = df.isnull().sum().sum()

missing_removed = missing_before - missing_after

# -----------------------------
# Duplicate Records Removed
# -----------------------------

duplicate_removed = df.duplicated().sum()

df = df.drop_duplicates()

# -----------------------------
# Invalid Transactions Removed
# -----------------------------

before = len(df)

df = df[(df["Quantity"] > 0) &
        (df["Price Per Unit"] > 0)]

after = len(df)

invalid_removed = before - after

# -----------------------------
# Save Cleaned Dataset
# -----------------------------

df.to_csv("cleaned_dataset.csv", index=False)

# -----------------------------
# Summary
# -----------------------------

print("\nSUMMARY")
print("Missing Values Removed =", missing_removed)
print("Duplicate Records Removed =", duplicate_removed)
print("Invalid Transactions Removed =", invalid_removed)

print("\nCleaned dataset saved as cleaned_dataset.csv")"""
import pandas as pd

df = pd.read_csv("dirty_cafe_sales.csv")

# Convert columns to numeric
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors="coerce")

# Find invalid transactions
invalid = df[(df["Quantity"] <= 0) |
             (df["Price Per Unit"] <= 0)]

print("Invalid Transactions:")
print(invalid)
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors="coerce")

# Count records before cleaning
before = len(df)

# Remove invalid transactions
df = df[(df["Quantity"] > 0) &
        (df["Price Per Unit"] > 0)]

# Count records after cleaning
after = len(df)

print("Invalid Transactions Removed =", before - after)

print("\nCleaned Dataset:")
print(df.head())
