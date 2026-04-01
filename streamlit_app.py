import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
from pathlib import Path

# Define the exact columns your model expects (19 features)
expected_columns = [
    'is_new_device', 'login_attempts', 'failed_logins', 'session_duration',
    'port_accessed', 'payload_size_kb', 'data_exfiltration_volume', 'access_frequency',
    'is_outside_business_hours', 'time_of_day', 'country_USA',
    'protocol_TCP', 'protocol_UDP',
    'resource_accessed_/backup', 'resource_accessed_/config',
    'resource_accessed_/data', 'resource_accessed_/files',
    'resource_accessed_/home', 'resource_accessed_/login'
]


# Load trained model
model = joblib.load("isolation_forest_model.pkl")

# Stream logs from CSV instead of generating fake ones
def log_stream_from_csv(file_path):
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        yield row.to_dict()

# Alert generation logic based on actual features
def generate_alert(log):
    alerts = []
    if log.get('data_exfiltration_volume', 0) > 1.5:
        alerts.append("High data exfiltration")
    if log.get('access_frequency', 0) > 1:
        alerts.append("Frequent access attempts")
    if log.get('is_outside_business_hours', 0) == 1:
        alerts.append("Access outside business hours")
    if log.get('resource_accessed_/config', 0) == 1:
        alerts.append("Sensitive config accessed")
    if log.get('payload_size_kb', 0) < -1:
        alerts.append("Suspiciously small payload")
    return ", ".join(alerts) if alerts else "Generic anomaly"

# Store alert to history CSV
def log_alert(log, reason):
    log['alert_reason'] = reason
    pd.DataFrame([log]).to_csv("alert_history.csv", mode='a', header=not Path("alert_history.csv").exists(), index=False)

# Streamlit UI setup
st.set_page_config(page_title="AI Threat Detection", layout="wide")
st.title("🛡️ Real-Time AI Threat Detection Dashboard")
placeholder = st.empty()

# Real-time processing of logs from CSV
for log in log_stream_from_csv("processed_logs.csv"):
    df_log = pd.DataFrame([log])  # ✅ Use all 29 columns

    score = model.decision_function(df_log.values)[0]
    prediction = model.predict(df_log.values)[0]


    log_display = log.copy()
    log_display['anomaly_score'] = round(score, 5)

    with placeholder.container():
        if prediction == -1:
            reason = generate_alert(log)
            log_alert(log_display, reason)
            st.error(f"🚨 Threat detected! Reason: {reason}", icon="🚨")
        else:
            st.success("✅ Normal log", icon="✅")
        st.write(pd.DataFrame([log_display]))

    time.sleep(0.5)
