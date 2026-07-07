import os
import json
import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/zameen-updated.csv")

print("=" * 50)
print("DATA VALIDATION REPORT")
print("=" * 50)

rows, columns = df.shape

print(f"\nRows: {rows}")
print(f"Columns: {columns}")

print("\nData Types:")
print(df.dtypes)

missing_values = df.isnull().sum()

print("\nMissing Values:")
print(missing_values)

duplicate_rows = int(df.duplicated().sum())

print("\nDuplicate Rows:")
print(duplicate_rows)

print("\nTarget Column (price):")
print(df["price"].describe())

negative_prices = int((df["price"] < 0).sum())

print(f"\nNegative Prices: {negative_prices}")

# Create reports folder
os.makedirs("reports", exist_ok=True)

# Save validation report
report = {
    "rows": rows,
    "columns": columns,
    "missing_values": {k: int(v) for k, v in missing_values.items()},
    "duplicate_rows": duplicate_rows,
    "negative_prices": negative_prices,
    "data_types": {k: str(v) for k, v in df.dtypes.items()}
}

with open("reports/validation_report.json", "w") as f:
    json.dump(report, f, indent=4)

print("\nValidation report saved successfully!")
print("Location: reports/validation_report.json")