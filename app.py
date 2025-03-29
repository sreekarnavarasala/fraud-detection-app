import streamlit as st
import joblib
import numpy as np


model = joblib.load("fraud_detection_model.pkl")

st.title("Fraud Detection App")
st.write("Enter transaction details to check for fraud.")

step = st.number_input("Step", min_value=0)
type_ = st.selectbox("Transaction Type", ["CASH_OUT", "TRANSFER"])
amount = st.number_input("Transaction Amount", min_value=0.0)
oldbalanceOrg = st.number_input("Old Balance (Origin)", min_value=0.0)
newbalanceOrig = st.number_input("New Balance (Origin)", min_value=0.0)
oldbalanceDest = st.number_input("Old Balance (Destination)", min_value=0.0)
newbalanceDest = st.number_input("New Balance (Destination)", min_value=0.0)

type_encoded = 1 if type_ == "TRANSFER" else 0  # Change based on your encoding

if st.button("Check for Fraud"):
    features = np.array([[step, type_encoded, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest]])
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("⚠️ This transaction is potentially FRAUDULENT!")
    else:
        st.success("✅ This transaction is LEGITIMATE.")

