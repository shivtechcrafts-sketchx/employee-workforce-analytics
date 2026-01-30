import pandas as pd
from src.config import DATA_CLEAN_PATH


def generate_metrics():
    df = pd.read_csv(DATA_CLEAN_PATH)

    metrics = {
        "total_employees": len(df),
        "avg_age": round(df['age'].mean(), 2),
        "avg_salary": round(df['salary'].mean(), 2),
        "male_ratio": round((df['gender'] == "Male").mean() * 100, 2),
        "female_ratio": round((df['gender'] == "Female").mean() * 100, 2),
    }

    print("\n[INFO] Key Workforce Metrics:\n")
    for k, v in metrics.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    generate_metrics()
