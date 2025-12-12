import streamlit as st
import numpy as np
import pandas as pd
import joblib
import warnings
warnings.filterwarnings("ignore")

@st.cache_resource
def load_model():
    return joblib.load("best_model.pkl")

model = load_model()


st.title("ScoreSight — Student Exam Predictor 🎯")

study_hours = st.slider("Study Hours per Day:",0.0,16.0,2.0)
attendance= st.slider("Enter Attendance Percentage:",0.0,100.0,80.0)
mental_health = st.slider("Mental Health Rating (1-10):",1,10,5)
sleep_hours = st.slider("Sleep Hours per Day:",0.0,12.0,7.0)
part_time_job = st.selectbox("Part-time Job (Yes/No):", options=["Yes", "No"])


ptj_encoded = 1 if part_time_job == "Yes" else 0


if st.button("Predict Exam Marks"):
    input_data = np.array([[study_hours, attendance, mental_health, sleep_hours, ptj_encoded]], dtype=float)
    pred = model.predict(input_data)        # shape (1,)
    pred = np.clip(pred, 0, 100)            # clamp
    st.success(f"Predicted Exam Marks: {pred[0]:.2f}")
    
    
