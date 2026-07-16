import os
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder


class DataPreprocessing:

    def __init__(self):
        self.input_path = "data/raw/zameen-updated.csv"
        self.output_path = "data/processed/processed_data.csv"
        self.encoder_path = "models/label_encoders.pkl"

    def preprocess_data(self):

        # Load dataset
        df = pd.read_csv(self.input_path)

        print("=" * 60)
        print("Starting Data Preprocessing...")
        print("=" * 60)

        # Drop unnecessary columns
        columns_to_drop = [
            "property_id",
            "location_id",
            "page_url",
            "date_added",
            "agency",
            "agent",
            "area"
        ]

        df.drop(columns=columns_to_drop, inplace=True, errors="ignore")

        # Remove duplicates
        before = len(df)
        df.drop_duplicates(inplace=True)
        print(f"Duplicate rows removed : {before - len(df)}")

        # Remove zero-price rows
        before = len(df)
        df = df[df["price"] > 0]
        print(f"Zero-price rows removed : {before - len(df)}")

        # Fill missing values
        for col in df.columns:
            if df[col].dtype == "object":
                df[col] = df[col].fillna(df[col].mode()[0])
            else:
                df[col] = df[col].fillna(df[col].median())

        # -----------------------------
        # Encode categorical columns
        # -----------------------------
        encoders = {}

        categorical_columns = df.select_dtypes(include="object").columns

        for col in categorical_columns:

            encoder = LabelEncoder()

            df[col] = encoder.fit_transform(
                df[col].astype(str)
            )

            encoders[col] = encoder

        # -----------------------------
        # Save Encoders
        # -----------------------------
        os.makedirs("models", exist_ok=True)

        joblib.dump(
            encoders,
            self.encoder_path
        )

        print(f"Label Encoders Saved : {self.encoder_path}")

        # -----------------------------
        # Save Processed Dataset
        # -----------------------------
        os.makedirs("data/processed", exist_ok=True)

        df.to_csv(
            self.output_path,
            index=False
        )

        print("=" * 60)
        print("Data Preprocessing Completed Successfully")
        print(f"Final Shape : {df.shape}")
        print(f"Saved File  : {self.output_path}")
        print("=" * 60)

        return df


if __name__ == "__main__":

    preprocessing = DataPreprocessing()
    processed_df = preprocessing.preprocess_data()

    print(processed_df.head())