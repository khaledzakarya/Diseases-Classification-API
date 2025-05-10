import streamlit as st
import requests

st.title("🩺 Prognosis Prediction App")

# Input fields
st.subheader("Enter Patient Information:")

age = st.number_input("Age", min_value=0, max_value=120)
gender = st.selectbox("Gender", ["Male", "Female"])
Temperature_C = st.number_input("Temperature (°C)", min_value=-20.0, max_value=45.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0)
Wind_Speed_kmh = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=100.0)

# Binary symptoms checkboxes
symptoms = [
    "nausea", "joint_pain", "abdominal_pain", "high_fever", "chills", "fatigue", "runny_nose",
    "pain_behind_the_eyes", "dizziness", "headache", "chest_pain", "vomiting", "cough",
    "hiv_aids", "nasal_polyps", "asthma", "high_blood_pressure", "severe_headache", "weakness",
    "trouble_seeing", "fever", "body_aches", "sore_throat", "sneezing", "diarrhea",
    "rapid_breathing", "rapid_heart_rate", "pain_behind_eyes", "swollen_glands", "rashes",
    "sinus_headache", "facial_pain", "shortness_of_breath", "reduced_smell_and_taste",
    "skin_irritation", "itchiness", "throbbing_headache", "confusion", "back_pain",
    "knee_ache"
]

symptom_data = {}
for symptom in symptoms:
    symptom_data[symptom] = int(st.checkbox(symptom.replace("_", " ").title()))

# Submit button
if st.button("Predict Prognosis"):
    # Prepare data
    payload = {
        "Age": age,
        "Gender": gender,
        "Temperature": Temperature_C,
        "Humidity": humidity,
        "Wind_Speed": Wind_Speed_kmh,
        **symptom_data
    }

    # Send request to FastAPI
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f"🧠 Predicted Prognosis: **{result['predicted_prognosis']}**")
        else:
            st.error("❌ Error: Could not get prediction from API.")
    except Exception as e:
        st.error(f"⚠️ Exception: {e}")