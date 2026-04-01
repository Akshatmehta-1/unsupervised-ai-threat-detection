# unsupervised-ai-threat-detection

# 🛡️ AI-Powered Cybersecurity Threat Detection System

This project is an **unsupervised machine learning system** designed to detect suspicious user behavior and potential cyber threats based on activity logs.

---

## 🚀 What This Project Does

* Analyzes user activity logs
* Learns normal behavior patterns
* Detects anomalies (unusual behavior)
* Flags them as potential cyber threats

---

## 🧠 Core Idea (Explain This in Interview)

Traditional systems need labeled attack data.

This system:
👉 **does NOT need labels**

It uses **unsupervised learning** to:

* Learn what “normal” looks like
* Detect anything that deviates from it

---

## ⚙️ How It Works (Step-by-Step)

### 1. Data Collection

We use log-based data such as:

* User activity
* Request patterns
* Behavioral signals

Files:

* `unsupervised_logs.csv`
* `processed_logs.csv`

---

### 2. Data Preprocessing

* Cleaned the dataset
* Selected important features
* Converted categorical data into usable format

---

### 3. Model Used

👉 **Isolation Forest**

Why?

* Works well for anomaly detection
* Efficient on large datasets
* Doesn’t require labeled data

---

### 4. Model Training

* Model trained on normal + mixed behavior data
* Learns patterns of normal activity
* Saves model using `joblib`

File:

* `isolation_forest_model.pkl`

---

### 5. Prediction Logic

For each new log:

* Model calculates anomaly score
* Output:

  * `0` → Normal
  * `1` → Suspicious

---

### 6. Output Files

* `flagged_suspicious_logs.csv` → detected threats
* `alert_history.csv` → tracking suspicious activity

---

## 🖥️ Application (Streamlit)

The app provides:

* Interface to analyze logs
* Displays suspicious activity
* Shows results in real-time

Run app:

```bash
streamlit run app.py
```

---

## 🛠 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit

---

## 📂 Project Structure

* `streamlit_app.py` → Streamlit interface
* `Unsupervised_model.ipynb/` → trained model
* `processed_logs.csv/` → log datasets
* `retrain_model.py` → retraining script
* 'isolation_forest_model.pkl/' → Trained Isolation Forest model
* 'requirements.txt/' → List of dependencies required to run the project


---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Future Improvements

* Real-time log streaming
* Auto-block malicious IPs
* Dashboard visualization
* Integration with SIEM tools

---

## 👤 Author

Akshat Mehta
