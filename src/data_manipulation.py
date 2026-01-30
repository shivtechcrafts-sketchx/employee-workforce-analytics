import pandas as pd
from src.config import DATA_CLEAN_PATH


def manipulate_data():
    df = pd.read_csv(DATA_CLEAN_PATH)

    # Feature engineering
    df['age_group'] = pd.cut(df['age'], bins=[0,25,35,60], labels=['Young','Mid','Senior'])

    # Aggregations
    city_salary = df.groupby('city')['salary'].mean().sort_values(ascending=False)

    print("\n[INFO] Average Salary by City:\n")
    print(city_salary)

if __name__ == "__main__":
    manipulate_data()
