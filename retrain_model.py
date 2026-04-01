# retrain_model.py
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load all features
df = pd.read_csv("processed_logs.csv")


# Train the model
model = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
model.fit(df)

# Save it for Streamlit
joblib.dump(model, "isolation_forest_model.pkl")

print("✅ Model retrained and saved.")
