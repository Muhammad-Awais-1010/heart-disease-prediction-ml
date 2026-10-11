import pickle
from pathlib import Path
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "awais_heart_model.pkl"

st.set_page_config(page_title="CardioCheck | Heart Disease Demo", page_icon="❤️", layout="wide")
st.markdown("""<style>
.main {background-color:#f6f8fc;}
.block-container {padding-top: 2rem; max-width: 1100px;}
.hero {padding: 1.4rem 1.6rem; border-radius: 18px; background: linear-gradient(120deg,#132a4a,#246b78); color: white; margin-bottom: 1rem;}
.hero h1 {color:white; margin-bottom:.3rem;}
.smallnote {color:#596579; font-size:.92rem;}
</style>""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as file:
        return pickle.load(file)

st.markdown('<div class="hero"><h1>CardioCheck</h1><p>Heart disease prediction demonstration · AIC354</p></div>', unsafe_allow_html=True)
st.write("Enter four health attributes to see the model's predicted class. This is an educational machine-learning demonstration, not a medical diagnosis.")

left, right = st.columns([1.05, 0.95], gap="large")
with left:
    st.subheader("Patient attributes")
    with st.form("prediction_form"):
        age = st.slider("Age (years)", 20, 90, 54)
        sex = st.radio("Sex code", options=[0, 1], format_func=lambda x: "Female (0)" if x == 0 else "Male (1)", horizontal=True)
        trestbps = st.number_input("Resting blood pressure (mm Hg)", min_value=80, max_value=220, value=130, step=1)
        chol = st.number_input("Serum cholesterol (mg/dl)", min_value=100, max_value=600, value=240, step=1)
        submitted = st.form_submit_button("Run prediction", type="primary", use_container_width=True)
with right:
    st.subheader("About the model")
    st.metric("Input attributes", "4")
    st.write("The model uses age, sex, resting blood pressure, and serum cholesterol. It was trained on the Cleveland subset of the UCI Heart Disease dataset with a stratified train/test split.")
    st.info("A positive result means the model predicts the dataset's disease-present class. Consult a qualified healthcare professional for real health concerns.")

if submitted:
    row = pd.DataFrame([[age, sex, trestbps, chol]], columns=["age", "sex", "trestbps", "chol"])
    prediction = int(load_model().predict(row)[0])
    st.divider()
    if prediction == 1:
        st.error("Model result: Heart disease predicted present")
    else:
        st.success("Model result: Heart disease predicted absent")
    st.caption("Prediction only; not a clinical assessment.")

st.divider()
st.markdown('<p class="smallnote">Student: Muhammad Awais · FA24-BSE-076 · Section: BSE-A</p>', unsafe_allow_html=True)
