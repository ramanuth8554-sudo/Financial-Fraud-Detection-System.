import streamlit as st  
import pandas as pd
import joblib

model = joblib.load('fraud_detection_model.pkl')

st.title('Fraud Detection Prediction App')

st.markdown("Please enter the trainsaction details and Click the button (Predict)")

st.divider()

transaction_type = st.selectbox("Transaction Type",["PAYMENT","TRANSFER","CASH_OUT","DEPOSIT" ])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New balance (Receiver)", min_value=0.0, value=0.0)
  


if st.button("Predict"):
  input_data = pd.DataFrame([{
    'type': transaction_type,
    'amount': amount,
    'oldbalanceOrg': oldbalanceOrg,
    'newbalanceOrig': newbalanceOrig,
    'oldbalanceDest': oldbalanceDest,
    'newbalanceDest': newbalanceDest
  }])
  
  prediction = model.predict(input_data)[0]
  
  st.subheader(f"Prediction Result: {int(prediction)}")
  
  if prediction == 1:
    st.error("This transaction can be fraud")
    
  else:
    st.success("This transaction look like it's not fraud")
  
    
