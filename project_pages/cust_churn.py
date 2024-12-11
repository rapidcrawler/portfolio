import streamlit as st
import pickle
import pandas as pd
import numpy as np

def cust_churn():
    st.title("Customer Churn Prediction 📉")
    st.divider()

    model_path = "./project_pages/pickles/cust_churn_xgb_clf.pkl"
    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    # Function to process input data based on feature engineering
    def preprocess_input(data):
        # Interaction between balance and number of products
        data['Balance_Products_Interaction'] = data['Balance'] * data['NumOfProducts']
    
        # Age group based on the 'Age' to capture life stages
        data['Age_Group'] = pd.cut(data['Age'], bins=[0, 18, 35, 55, 100], labels=['Teen', 'Young Adult', 'Adult', 'Senior'])
    
        # Credit Score into categories
        data['Credit_Category'] = pd.cut(data['CreditScore'], bins=[0, 580, 670, 740, 800, 850], 
                                         labels=['Poor', 'Fair', 'Good', 'Very Good', 'Excellent'])
    
        # Feature indicating the overall engagement score
        data['Engagement_Score'] = (data['HasCrCard'] + data['IsActiveMember']) * 0.5
    
        # One-hot encode categorical variables
        data = pd.get_dummies(data, columns=['Geography', 'Gender', 'Age_Group', 'Credit_Category'], drop_first=False)
    
        return data
    
    # Streamlit app
    st.title("Customer Churn Prediction Form")
    
    # Create a form for user input
    with st.form("churn_form"):
        st.subheader("Customer Details")
    
        # Inputs for numeric features
        CreditScore = st.number_input("Credit Score", min_value=300, max_value=850, step=1)
        Age = st.number_input("Age", min_value=0, max_value=100, step=1)
        Tenure = st.number_input("Tenure (years)", min_value=0, max_value=10, step=1)
        Balance = st.number_input("Balance", min_value=0.0, step=100.0)
        NumOfProducts = st.number_input("Number of Products", min_value=1, max_value=5, step=1)
        EstimatedSalary = st.number_input("Estimated Salary", min_value=0.0, step=1000.0)
    
        # Inputs for categorical features
        Geography = st.selectbox("Geography", options=['France', 'Germany', 'Spain'])
        Gender = st.selectbox("Gender", options=['Male', 'Female', 'Neutral'])
    
        # Inputs for binary features
        HasCrCard = st.radio("Has Credit Card?", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
        IsActiveMember = st.radio("Is Active Member?", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
    
        # Submit button
        submitted = st.form_submit_button("Prepare Data")
    
    # Process the input after form submission
    if submitted:
        # Create a dataframe from input
        input_data = {
            'CreditScore': [CreditScore],
            'Age': [Age],
            'Tenure': [Tenure],
            'Balance': [Balance],
            'NumOfProducts': [NumOfProducts],
            'EstimatedSalary': [EstimatedSalary],
            'Geography': [Geography],
            'Gender': [Gender],
            'HasCrCard': [HasCrCard],
            'IsActiveMember': [IsActiveMember]
        }
        input_df = pd.DataFrame(input_data)
    
        # Preprocess the input data
        processed_data = preprocess_input(input_df)
    
        # Show processed data
        st.subheader("Processed Data")
        st.write(processed_data)

        # Reshape for Prediction
        input_data = input_data.reshape(1, -1)

        # Predict Customer Churn
        prediction = model.predict(input_data)
        if prediction[0] == 1:
            st.success('💔 Yes, the customer is likely to churn.')
        else:
            st.success('🎯 No, the customer is not likely to churn.')

    st.divider()
