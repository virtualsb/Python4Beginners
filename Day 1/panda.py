import pandas as pd
import os

file_path = os.path.join("dataset", "data.csv")


if os.path.isfile(file_path):
    print(f"📄 Loading file: {file_path}")
    df = pd.read_csv(file_path)

    # Basic exploration
    print("\n🔹 First 5 rows:")
    print(df.head())

    print("\n🔹 Info:")
    print(df.info())

    print("\n🔹 Summary statistics:")
    print(df.describe())

    print("\n🔹 Column names:")
    print(df.columns.tolist())

    print("\n🔹 Missing values per column:")
    print(df.isnull().sum())

else:
    print(f"❌ File not found: {file_path}")
