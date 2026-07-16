import pandas as pd
from datetime import datetime

df = pd.read_csv("data/raw/zameen-updated.csv")

df["event_timestamp"] = datetime.now()

df.to_csv("feature_store/feature_repo/data/zamee_features.csv", index=False)

print("Dataset prepared for Feast.")
