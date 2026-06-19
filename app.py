import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="centered"
)

# ---------------- LOAD FILES ----------------

model = joblib.load("SVM_diabetes.pkl")
scaler = joblib.load("diabetes_scaler.pkl")
expected_columns = joblib.load("diabetes_columns.pkl")

# ---------------- TITLE ----------------
st.markdown(
    """
    <h1 style='text-align:center;'>
        🩺 Diabetes Prediction System
    </h1>
    <h4 style='text-align:center; color:gray;'>
        By Minal
    </h4>
    """,
    unsafe_allow_html=True
)
st.markdown("### Check your diabetes risk using health information")

# ---------------- PERSONAL INFORMATION ----------------
st.info(
    "Please enter your health information below..."
)
st.subheader("👤 Personal Information")

age = st.slider(
    "Age",
    min_value=18,
    max_value=100,
    value=40
)

# ---------------- PREGNANCY INFORMATION ----------------

st.subheader("🤰 Pregnancy Information")

pregnancies = st.selectbox(
    "Number of Pregnancies",
    options=list(range(0, 21))
)

# ---------------- BODY MEASUREMENTS ----------------

st.subheader("⚖️ Body Measurements")

col1, col2 = st.columns(2)

with col1:
    weight = st.number_input(
        "Weight (kg)",
        min_value=20.0,
        max_value=250.0,
        value=60.0
    )

with col2:
    height = st.number_input(
        "Height (cm)",
        min_value=100.0,
        max_value=250.0,
        value=165.0
    )

# BMI Calculation
bmi = weight / ((height / 100) ** 2)

st.success(f"Calculated BMI: {bmi:.2f}")

# ---------------- DPF ----------------

st.subheader("🧬 Diabetes Pedigree Function")

dpf = st.number_input(
    "Diabetes Pedigree Function",
    min_value=0.0,
    max_value=3.0,
    value=0.47,
    format="%.3f",
    help="Represents hereditary diabetes risk. If unknown, keep the default value."
)

# ---------------- HEALTH DETAILS ----------------

st.subheader("🩸 Health Details")

col1, col2 = st.columns(2)

with col1:
    glucose = st.slider(
        "Glucose Level",
        min_value=50,
        max_value=250,
        value=120
    )

    blood_pressure = st.number_input(
        "Blood Pressure",
        min_value=40,
        max_value=200,
        value=80
    )

with col2:
    skin_thickness = st.number_input(
        "Skin Thickness",
        min_value=0,
        max_value=100,
        value=20,
        help="If unknown, keep the default value."
    )

    insulin = st.number_input(
        "Insulin Level",
        min_value=0,
        max_value=900,
        value=80,
        help="If unknown, keep the default value."
    )

# ---------------- PREDICTION ----------------

if st.button("🔍 Predict Diabetes Risk", use_container_width=True):

    input_df = pd.DataFrame({
        "Pregnancies": [pregnancies],
        "Glucose": [glucose],
        "BloodPressure": [blood_pressure],
        "SkinThickness": [skin_thickness],
        "Insulin": [insulin],
        "BMI": [bmi],
        "DiabetesPedigreeFunction": [dpf],
        "Age": [age]
    })

    input_df = input_df[expected_columns]

    scaled_data = scaler.transform(input_df)

    prediction = model.predict(scaled_data)

    st.divider()
    st.subheader("📋 Prediction Result")

    if prediction[0] == 1:
        st.error("⚠️ The person is likely Diabetic")
        st.warning(
            "Please consult a healthcare professional for proper diagnosis and treatment."
        )
    else:
        st.success("✅ The person is unlikely to be Diabetic")