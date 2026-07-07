import os
import pandas as pd


class DataIngestion:
    def __init__(self):
        self.data_path = "data/raw/zameen-updated.csv"

    def ingest_data(self):
        # Check if file exists
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Dataset not found: {self.data_path}")

        # Read dataset
        df = pd.read_csv(self.data_path)

        print("=" * 50)
        print("Data Ingestion Completed Successfully")
        print(f"Dataset Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        print("=" * 50)

        return df


if __name__ == "__main__":
    ingestion = DataIngestion()
    df = ingestion.ingest_data()
    print(df.head())