import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="FinSight - Fraud Detection", page_icon="🏦", layout="centered")

model = joblib.load("models/fraud_detection_model.pkl")

st.title("FinSight Banking Analytics")
st.subheader("AI-Powered Credit Card Fraud Detection")
st.markdown("---")

st.markdown("### Enter Transaction Details")
col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("Transaction Amount ($)", min_value=0.0, value=100.0)
    v1 = st.slider("V1", -5.0, 5.0, 0.0)
    v2 = st.slider("V2", -5.0, 5.0, 0.0)
    v3 = st.slider("V3", -5.0, 5.0, 0.0)
    v4 = st.slider("V4", -5.0, 5.0, 0.0)
    v5 = st.slider("V5", -5.0, 5.0, 0.0)
    v6 = st.slider("V6", -5.0, 5.0, 0.0)
    v7 = st.slider("V7", -5.0, 5.0, 0.0)

with col2:
    v8 = st.slider("V8", -5.0, 5.0, 0.0)
    v9 = st.slider("V9", -5.0, 5.0, 0.0)
    v10 = st.slider("V10", -5.0, 5.0, 0.0)
    v11 = st.slider("V11", -5.0, 5.0, 0.0)
    v12 = st.slider("V12", -5.0, 5.0, 0.0)
    v13 = st.slider("V13", -5.0, 5.0, 0.0)
    v14 = st.slider("V14", -5.0, 5.0, 0.0)
    v15 = st.slider("V15", -5.0, 5.0, 0.0)

v16=v17=v18=v19=v20=v21=v22=v23=v24=v25=v26=v27=v28=0.0

scaler = StandardScaler()
amount_scaled = scaler.fit_transform([[amount]])[0][0]

st.markdown("---")
if st.button("Detect Fraud", use_container_width=True):
    features = [[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,amount_scaled]]
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0]
    st.markdown("### Result")
    if prediction == 1:
        st.error(f"FRAUDULENT TRANSACTION DETECTED! Probability: {probability[1]*100:.2f}%")
    else:
        st.success(f"LEGITIMATE TRANSACTION. Safe Probability: {probability[0]*100:.2f}%")

st.markdown("---")
st.markdown("### Model Performance")
col1, col2, col3 = st.columns(3)
col1.metric("ROC AUC Score", "0.9819")
col2.metric("Precision", "94%")
col3.metric("Total Transactions", "215,945")
st.caption("Built by Mohammed Shawaiz Hussain | FinSight Banking Analytics")
