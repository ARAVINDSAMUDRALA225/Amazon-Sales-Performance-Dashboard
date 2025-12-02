import pandas as pd

# ----------------------------------------
# Amazon Sales Data - Data Cleaning Script
# ----------------------------------------
# Objective:
# 1. Load raw CSV dataset
# 2. Remove unnecessary columns and bad data
# 3. Standardize and prepare fields for analysis
# 4. Export cleaned dataset for Power BI dashboard
# ----------------------------------------

# 1️.Load the dataset into pandas DataFrame
print("Loading data...")
df = pd.read_csv("C:\\Users\\Aravind\\OneDrive\\Attachments\\Desktop\\amazon_sales_analysis\\Amazon__Sale__Report.csv")

# 2️.Remove unwanted index column (if present)
# 'index' column does not provide any useful information
if "index" in df.columns:
    df = df.drop(columns=["index"])

# 3.Convert Date column into proper datetime format
# 'errors=coerce' converts invalid dates into NaT (not a valid date)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# 4.Remove rows where Date conversion failed (NaT)
# Invalid or blank dates are not useful for trend analysis
df = df.dropna(subset=["Date"])

# 5.Drop unnecessary or high-null columns
# These fields have too many missing values / no analytical need
cols_to_drop = ["fulfilled-by", "New", "PendingS"]
df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])

# 6.Remove rows where Amount is missing
# Sales amount is mandatory for any business insight
df = df.dropna(subset=["Amount"])

# 7.Remove rows where shipping city or state information is missing
# Location fields are required for geographic analysis
df = df.dropna(subset=["ship-city", "ship-state"])

# 8.Create a Month field for monthly trend visualization in Power BI
# Converts date into 'YYYY-MM' format (Monthly level)
df["Month"] = df["Date"].dt.to_period("M").astype(str)

# 9.Save the cleaned dataset into a new CSV file
# This cleaned file will be used in SQL loading and Power BI visualization
output_file = "Amazon_Sales_Cleaned.csv"
df.to_csv(output_file, index=False)

print("Cleaning done successfully! 👍")
print("Final dataset shape:", df.shape)
print(f"Cleaned data saved as: {output_file}")

