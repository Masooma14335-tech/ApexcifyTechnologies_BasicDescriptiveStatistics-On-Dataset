import pandas as pd
import seaborn as sns

datasets = {
    "Tips": sns.load_dataset('tips'),
    "Iris": sns.load_dataset('iris'),
    "Titanic": sns.load_dataset('titanic')
}

def analyze_dataset(df, name):
    print(f"\n{'='*60}")
    print(f"Dataset: {name}")
    print(f"{'='*60}\n")
    
    print("First 10 rows:")
    print(df.head(10), "\n")
    
    print("Missing Values:")
    missing = df.isnull().sum()
    for col, val in missing.items():
        if val > 0:
            print(f"★ {col}: {val} missing values")
        else:
            print(f"{col}: {val}")
    print("\n")
    
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) > 0:
        print("Numeric Columns Statistics:\n")
        for col in numeric_cols:
            col_data = df[col][df[col] != 0].dropna()
            if len(col_data) == 0:
                continue
            print(f"Column: {col}")
            print("Mean:", col_data.mean())
            print("Median:", col_data.median())
            print("Mode:", col_data.mode().values)
            print("Min:", col_data.min())
            print("Max:", col_data.max())
            print("Standard Deviation:", col_data.std())
            print("-"*40)
    else:
        print("No numeric columns found.")

for name, df in datasets.items():
    analyze_dataset(df, name)
