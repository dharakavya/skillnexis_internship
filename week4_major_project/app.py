import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("loan_approval_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="wide"
)

# Application title
st.title("🏦 Bank Loan Approval Prediction")
st.write(
    "Enter the applicant details below to predict "
    "whether the loan application is likely to be approved."
)

st.info(
    "This is an educational machine-learning project. "
    "Predictions are not actual bank decisions."
)

# Input form
with st.form("loan_prediction_form"):

    st.subheader("Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        married = st.selectbox(
            "Marital Status",
            ["Yes", "No"]
        )

        dependents = st.selectbox(
            "Number of Dependents",
            ["0", "1", "2", "3+"]
        )

    with col2:
        education = st.selectbox(
            "Education",
            ["Graduate", "Not Graduate"]
        )

        self_employed = st.selectbox(
            "Self Employed",
            ["No", "Yes"]
        )

    st.subheader("Financial Information")

    col3, col4 = st.columns(2)

    with col3:
        applicant_income = st.number_input(
            "Applicant Income",
            min_value=0,
            value=5000,
            step=500
        )

        coapplicant_income = st.number_input(
            "Coapplicant Income",
            min_value=0,
            value=0,
            step=500
        )

        loan_amount = st.number_input(
            "Loan Amount (dataset units)",
            min_value=1,
            value=100,
            step=10
        )

    with col4:
        loan_term = st.selectbox(
            "Loan Term (months)",
            [360, 180, 120, 240, 60, 36, 12]
        )

        credit_history = st.selectbox(
            "Credit History",
            [1.0, 0.0],
            format_func=lambda x: (
                "Good (1)" if x == 1.0
                else "Not Good (0)"
            )
        )

        property_area = st.selectbox(
            "Property Area",
            ["Urban", "Semiurban", "Rural"]
        )

    submitted = st.form_submit_button(
        "Predict Loan Status"
    )

# Make prediction
if submitted:

    input_data = pd.DataFrame([{
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": property_area
    }])

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == "Y":
        st.success("The model predicts: Loan Approved")
    else:
        st.error("The model predicts: Loan Rejected")

    # Show model probability, if supported
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(input_data)[0]
        classes = model.named_steps["classifier"].classes_

        approved_index = list(classes).index("Y")
        approved_probability = probabilities[approved_index]

        st.metric(
            "Model-estimated approval probability",
            f"{approved_probability * 100:.2f}%"
        )

        st.caption(
            "This is a model estimate, not a guarantee of approval "
            "or a calibrated measure of the applicant's true chances."
        )

    with st.expander("View submitted application details"):
        st.dataframe(input_data, use_container_width=True)