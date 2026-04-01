import streamlit as st
import requests

BASE_URL = "http://localhost:8000"

st.title("Expense Forecasting App")

if st.button("Get Prediction"):
    res = requests.get(f"{BASE_URL}/predict")
    st.write(res.json())