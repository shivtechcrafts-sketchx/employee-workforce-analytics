from src import data_cleaning, data_manipulation, data_modeling, visualization

def run_pipeline():
    data_cleaning.clean_data()
    data_manipulation.manipulate_data()
    data_modeling.generate_metrics()
    visualization.create_visuals()

if __name__ == "__main__":
    run_pipeline()
