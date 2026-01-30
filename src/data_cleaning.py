import pandas as pd
from src.config import DATA_RAW_PATH, DATA_CLEAN_PATH


def clean_data():
    df = pd.read_csv(DATA_RAW_PATH)

    # Standardize columns
    df.columns = df.columns.str.lower()

    # Handle missing values
    df['age'] = df['age'].fillna(df['age'].median())
    df['salary'] = df['salary'].fillna(df['salary'].mean())

    # Standardize text
    df['name'] = df['name'].str.title()
    df['city'] = df['city'].str.title()
    df['gender'] = df['gender'].str.title()

    # Remove duplicates
    df = df.drop_duplicates()

    df.to_csv(DATA_CLEAN_PATH, index=False)
    print("[INFO] Data cleaning completed.")

if __name__ == "__main__":
    clean_data()
    