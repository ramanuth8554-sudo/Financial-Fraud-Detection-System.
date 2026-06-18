# 📊 Financial Fraud Detection System using Machine Learning

An end-to-end Machine Learning project that detects fraudulent financial transactions using **Logistic Regression** and provides a user-friendly web interface built with **Streamlit**.

## 📌 Project Overview
Financial fraud causes billions of dollars in losses annually. This project aims to build a predictive model to classify whether a transaction is fraudulent (`isFraud = 1`) or valid (`isFraud = 0`). 

Based on Exploratory Data Analysis (EDA), fraudulent activities are heavily concentrated in specific transaction types: **TRANSFER** and **CASH_OUT**. Therefore, the model is highly optimized to analyze these specific behaviors.

## 🚀 Features
- **Data Preprocessing Pipeline:** Automated handling of numerical features using `StandardScaler` and categorical features using `OneHotEncoder` via Scikit-Learn's `ColumnTransformer`.
- **Machine Learning Model:** Trained on over 2.7 million targeted transaction records using `LogisticRegression`.
- **Interactive Web App:** A clean Streamlit interface allowing users to input transaction details and receive real-time fraud predictions.

## 📊 Model Performance
The model was evaluated using a 20% test split, achieving the following metrics:
- **Global Accuracy:** ~94.5%
- **Fraud Class Precision:** 1.00 (Zero False Alarms)
- **Fraud Class Recall:** 0.63 (Catches 63% of actual fraud cases)

*Note: The lower recall is due to extreme class imbalance (only 0.13% of the original dataset contains fraud cases).*

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-Learn, Seaborn, Matplotlib, Joblib
- **Deployment:** Streamlit

## 📦 Project Structure
```text
├── analysis_model.ipynb     # Jupyter Notebook containing EDA and Model Training
├── fraud_detection.py       # Streamlit Web Application
├── fraud_detection_model.pkl # Saved trained pipeline model (Joblib)
└── README.md                # Project documentation