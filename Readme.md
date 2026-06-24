#  Financial Fraud Detection System using Machine Learning

An end-to-end Data Science and Machine Learning project designed to detect fraudulent financial transactions using **Logistic Regression** and serve predictions via an interactive **Streamlit** web application.

---

##  Project Overview
Financial fraud amounts to billions of dollars in losses annually. This project builds a robust predictive pipeline to classify transaction logs as either fraudulent (`isFraud = 1`) or valid (`isFraud = 0`). 

Based on thorough Exploratory Data Analysis (EDA), fraudulent behaviors are heavily concentrated within specific transaction categories: **TRANSFER** and **CASH_OUT**. The model is heavily optimized and targeted toward filtering and predicting these exact transaction types.

##  Key Features
- **Targeted Data Pipeline:** Filters and analyzes high-risk transaction types (`TRANSFER` and `CASH_OUT`) from a massive dataset.
- **Automated Preprocessing:** Utilizes Scikit-Learn's `ColumnTransformer` featuring `StandardScaler` for numerical metrics and `OneHotEncoder` for categorical factors.
- **Optimized Classifiers:** Trained using an optimized `LogisticRegression` pipeline capable of managing high-volume data.
- **Interactive UI:** A functional web interface powered by **Streamlit** allowing live entries for instant prediction deployment.

##  Dataset 
- **Dataset Source:** You can access and download the raw data directly from Kaggle: [Kaggle Fraud Detection Dataset](https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset)

##  Model Architecture & Performance
The pipeline components and evaluation metrics consist of:
- **Feature Engineering:** Automated numerical scaling and string categorical mapping.
- **Global Accuracy:** **~94.5%** on targeted evaluation test splits.
- **Precision (Fraud Class):** **1.00** (Minimizes false positives/alarms perfectly).
- **Recall (Fraud Class):** **0.63** (Successfully flags 63% of real-time fraud attempts).

*Note: The model accounts for severe class imbalances inherent to financial fraud datasets.*

##  Tech Stack & Dependencies
- **Language:** Python
- **Core Libraries:** Pandas, NumPy, Scikit-Learn, Seaborn, Matplotlib, Joblib
- **Deployment:** Streamlit Web Framework

##  Project Structure
```text
├── .gitignore               # Excludes large raw data files from Git tracking
├── analysis_model.ipynb     # Jupyter Notebook containing data exploration & model training
├── fraud_detection.py       # Main Streamlit web application source code
├── fraud_detection_model.pkl # Compressed standalone trained pipeline model (Joblib format)
└── README.md                # Comprehensive project layout documentation
