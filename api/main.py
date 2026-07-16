import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException

from api.schemas import HouseData

app = FastAPI(
    title="House Price Prediction API",
    version="2.0"
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("models/best_model.pkl")

# -----------------------------
# Load Label Encoders
# -----------------------------
encoders = joblib.load("models/label_encoders.pkl")

# -----------------------------
# Load Scaler
# -----------------------------
scaler = joblib.load("models/scaler.pkl")


@app.get("/")
def home():
    return {"message": "House Price Prediction API is Running"}


@app.post("/predict")
def predict(data: HouseData):

    try:

        # -----------------------------
        # Encode Categorical Features
        # -----------------------------
        input_df = pd.DataFrame([{

            "property_type": encoders["property_type"].transform(
                [data.property_type]
            )[0],

            "location": encoders["location"].transform(
                [data.location]
            )[0],

            "city": encoders["city"].transform(
                [data.city]
            )[0],

            "province_name": encoders["province_name"].transform(
                [data.province_name]
            )[0],

            "latitude": data.latitude,

            "longitude": data.longitude,

            "baths": data.baths,

            "purpose": encoders["purpose"].transform(
                [data.purpose]
            )[0],

            "bedrooms": data.bedrooms,

            "Area Type": encoders["Area Type"].transform(
                [data.Area_Type]
            )[0],

            "Area Size": data.Area_Size,

            "Area Category": encoders["Area Category"].transform(
                [data.Area_Category]
            )[0]

        }])

        # -----------------------------
        # Scale Features
        # -----------------------------
        input_df = pd.DataFrame(
            scaler.transform(input_df),
            columns=input_df.columns
        )

        # -----------------------------
        # Debug (optional)
        # -----------------------------
        print("=" * 60)
        print(input_df)
        print("=" * 60)

        # -----------------------------
        # Prediction
        # -----------------------------
        prediction = model.predict(input_df)

        return {
            "Predicted Price": float(prediction[0])
        }

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=f"Invalid categorical value: {e}"
        )