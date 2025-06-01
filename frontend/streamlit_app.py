import streamlit as st
import requests
st.set_page_config(page_title="Mental Health Predictor", layout="centered")
st.write("App is running...")  # Add this to confirm Streamlit is working


st.title("🧠 Mental Health Treatment Predictor")

st.markdown("Fill in the form below to see if treatment may be needed.")

# Input form
age = st.slider("Age", 18, 70, 25)
gender = st.selectbox("Gender", ["Male (0)", "Female (1)", "Other (2)"])
family_history = st.radio("Family History of Mental Illness?", ["No (0)", "Yes (1)"])
work_interfere = st.selectbox("Work Interference", ["Never (0)", "Rarely (1)", "Sometimes (2)", "Often (3)"])
benefits = st.radio("Employer Provides Mental Health Benefits?", ["No (0)", "Yes (1)"])
care_options = st.radio("Has Access to Care Options?", ["No (0)", "Yes (1)"])
seek_help = st.radio("Encouraged to Seek Help?", ["No (0)", "Yes (1)"])
mental_conseq = st.radio("Afraid of Mental Health Consequences at Work?", ["No (0)", "Yes (1)"])

# Convert options to int
gender = int(gender[-2])
family_history = int(family_history[-2])
work_interfere = int(work_interfere[-2])
benefits = int(benefits[-2])
care_options = int(care_options[-2])
seek_help = int(seek_help[-2])
mental_conseq = int(mental_conseq[-2])

if st.button("🔍 Predict"):
    data = {
        "age": age,
        "gender": gender,
        "family_history": family_history,
        "work_interfere": work_interfere,
        "benefits": benefits,
        "care_options": care_options,
        "seek_help": seek_help,
        "mental_health_consequence": mental_conseq
    }

    try:
        response = requests.post("https://mental-health-ml-app.onrender.com/predict", json=data)

        result = response.json()["treatment_needed"]
        if result:
            st.error("⚠️ Prediction: Treatment Needed")
        else:
            st.success("✅ Prediction: No Treatment Needed")
    except:
        st.error("❌ Could not connect to the FastAPI backend. Is it running?")
