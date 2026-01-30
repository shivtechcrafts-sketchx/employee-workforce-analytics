import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.config import DATA_CLEAN_PATH, CHART_PATH


def create_visuals():
    df = pd.read_csv(DATA_CLEAN_PATH)

    # Salary distribution
    plt.figure()
    sns.histplot(df['salary'], bins=10)
    plt.title("Salary Distribution")
    plt.savefig(CHART_PATH + "salary_distribution.png")

    # City-wise salary
    plt.figure()
    df.groupby('city')['salary'].mean().plot(kind='bar')
    plt.title("Average Salary by City")
    plt.savefig(CHART_PATH + "city_salary.png")

    print("[INFO] Visualizations created.")

if __name__ == "__main__":
    create_visuals()
