import streamlit as st
import pickle
import numpy as np

def loan_eligibility():
    # Load your trained model from a pickle file
    model_path = "./project_pages/pickles/loan_approval_model.pkl"
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    
    # Function to calculate debt-to-income ratio
    def calculate_dti(income, current_emis_sum):
        if income == 0:
            return 0  # Avoid division by zero
        return current_emis_sum / income
    
    # Streamlit app setup
    st.title('Loan Eligibility 🏛️💰')
    st.subheader("📋 Fill Below Form To Check you Loan Eligibility")
    
    # User Inputs
    age = st.slider('Applicant Age', min_value=18, max_value=100, value=30)
    income = st.number_input('Applicant Income (Monthly)', min_value=0, value=30000)
    credit_score = st.number_input('Credit Score', min_value=300, max_value=850, value=650)
    loan_amount = st.number_input('Loan Amount', min_value=5000, max_value=1000000, value=50000)
    loan_tenure = st.number_input('Loan Tenure (Months)', min_value=6, max_value=360, value=60)
    current_emis_sum = st.number_input('Sum of Current EMIs', min_value=0, max_value=100000, value=5000)
    
    st.divider()

    st.subheader("Derived Data")
    # Calculate Debt-to-Income Ratio
    dti = calculate_dti(income, current_emis_sum)
    
    # Determine employment status based on income and display with specific formatting
    if income == 0:
        employment_status_value = 2  # Code for Unemployed in trained model
        st.markdown(
            '<p style="color:red; background-color:black; padding:5px; font-size:18px;">Employment Status: Unemployed</p>', 
            unsafe_allow_html=True)
    else:
        employment_status_value = 1  # Code for Employed in trained model
        st.markdown(
            '<p style="color:green; background-color:black; padding:5px; font-size:18px;">Employment Status: Employed</p>', 
            unsafe_allow_html=True)

    st.write(f'Debt-to-Income Ratio: {dti:.2f}')
    
    # Prepare input data for prediction
    input_data = np.array([[age, income, credit_score, loan_amount, loan_tenure, current_emis_sum, dti, employment_status_value]])
    
    # Predict loan approval
    if st.button('Predict Loan Approval'):
        prediction = model.predict(input_data)
        if prediction == 1:
            st.success('🎯 Loan Approved')
        else:
            st.error('💔 Loan Rejected')
