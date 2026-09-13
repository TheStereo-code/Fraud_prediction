import streamlit as st 
import pandas as pd
import joblib
import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "fraud_detection_pipeline.pkl"))

st.title("Fraud Prediction App")

st.markdown("PLease Enter the transaction details")

st.divider()

transaction_type = st.selectbox("Type of Transaction", ["PAYMENT", "TRANSFER", "CASHOUT","DEPOSIT"])
amount = st.number_input("Amount", min_value=0.0, value= 1000.00)

#Senders balance Amount details
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value = 0.0, value = 10000.00)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value = 0.0, value = 10000.0)

#Receivers balance Amount details
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value= 10000.00)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=10000.00)

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type" : transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction : '{int(prediction)}'")

    if prediction ==1:
        st.error("This is transaction is likely to be Fraud")
    else:
        st.success("This Transacction is likely not a Fraud")


