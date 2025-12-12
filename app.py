# app.py
import streamlit as st
import numpy as np
import pandas as pd
import joblib
import warnings
import os

warnings.filterwarnings("ignore")

st.set_page_config(page_title="ScoreSight — Student Exam Predictor", layout="centered")

st.title("ScoreSight — Student Exam Predictor 🎯")
st.write("Predict student exam marks from simple features. Run locally or on Streamlit Community Cloud.")

# ---------------------------
# Model loading with UI help
# ---------------------------
@st.cache_resource
def load_model(path="best_model.pkl"):
    if not os.path.exists(path):
        # Raise an informative error the UI can show
        raise FileNotFoundError(f"Model file not found at `{path}`. Make sure it's in the repo root.")
    model = joblib.load(path)
    return model

# Try load model and show helpful message if missing
model = None
try:
    with st.spinner("Loading model..."):
        model = load_model("best_model.pkl")
    st.success("Model loaded ✅")
except Exception as e:
    st.error(f"Could not load model: {e}")
    st.info("If your model is large (>100 MB) consider hosting it externally and download at startup.")
    # Prevent the app from continuing without model
    st.stop()

# ---------------------------
# Inputs
# ---------------------------
col1, col2 = st.columns(2)
with col1:
    study_hours = st.slider("Study Hours per Day:", 0.0, 16.0, 2.0, step=0.5)
    sleep_hours = st.slider("Sleep Hours per Day:", 0.0, 12.0, 7.0, step=0.5)
with col2:
    attendance = st.slider("Attendance Percentage:", 0.0, 100.0, 80.0, step=1.0)
    mental_health = st.slider("Mental Health Rating (1-10):", 1, 10, 5)

part_time_job = st.selectbox("Part-time Job (Yes/No):", options=["No", "Yes"])
ptj_encoded = 1 if part_time_job == "Yes" else 0

# Extra: show input summary
if st.checkbox("Show input values"):
    st.write({
        "Study hours": study_hours,
        "Attendance": attendance,
        "Mental health": mental_health,
        "Sleep hours": sleep_hours,
        "Part-time job": part_time_job
    })

# ---------------------------
# Prediction action
# ---------------------------
if st.button("Predict Exam Marks"):
    try:
        input_data = np.array([[study_hours, attendance, mental_health, sleep_hours, ptj_encoded]], dtype=float)
        pred = model.predict(input_data)        # shape (1,)
        pred = np.clip(pred, 0, 100)            # clamp
        st.success(f"Predicted Exam Marks: {pred[0]:.2f} / 100")
    except Exception as e:
        st.error(f"Prediction failed: {e}")


st.markdown("---")
st.caption("Repo: add README with usage instructions. Do not commit API keys or secrets.")
