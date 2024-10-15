import streamlit as st

def home():
    
    
    # Create two columns for image and name/introduction
    col1, col2 = st.columns([1, 3])  # Adjust the width ratio as needed
    
    # Add the image in the first column
    with col1:
        st.image("./imgs/jaspreetsingh.jpg", width=180)  # Adjust width as needed

    # Add name and introduction in the second column
    with col2:
    
        st.title("Jaspreet Singh - Senior Data Scientist")
        st.write("**6+ years of experience in building advanced analytical tools for Fortune100 companies like Walmart, JP Morgan, Dubai Government, lululemon, etc.**")    

        # Contact Information
        st.header("Contact Information")
        st.write("Email: [ai.jaspreetsingh@gmail.com](mailto:ai.jaspreetsingh@gmail.com)")
        st.write("LinkedIn: [linkedin.jaspreetblogs.in](http://linkedin.jaspreetblogs.in)")
        st.write("GitHub: [github.jaspreetblogs.in](http://github.jaspreetblogs.in)")


    # Summary Section
    st.header("Summary")
    st.write("""
    Lead Data Scientist with 6+ years of experience in building advanced analytical tools for Fortune100 companies like Walmart, JP Morgan,
    Emirates Global Aluminium, Dubai Department of Economy and Tourism, lululemon, etc. 
    Responsible for project planning and execution, team management, risk and issue management. 
    """)

    # Experience Section
    st.header("Experience")

    # Job 1: Maaloomatiia
    st.subheader("Senior Data Scientist - Maaloomatiia")
    st.write("**Sep 2023 - Present**")
    st.write("""
    - Built an NLP-based model to detect social trends, adopted by a global retail giant for the 2023 Black Friday sale.
    - Implemented an in-store video analytics solution using YOLO for customer behavior analysis, optimizing store operations.
    - Developed an N-BEATS model to forecast energy consumption in Dubai Metro, reducing resource shortages and saving $80K annually.
    - Delivered an LLM solution based on Llama3-8b for cab complaints classification, reducing acknowledgment lead time by 66.67%.
    - Created an XGBoost-based solution to predict overnight visitor arrivals for Dubai’s DET, optimizing marketing spends.
    - Implemented sentiment analysis and text summarization to provide actionable insights for Dubai’s immigration services.
    """)

    # Job 2: JP Morgan
    st.subheader("Senior Data Scientist - JP Morgan")
    st.write("**Feb 2022 - Sep 2023**")
    st.write("""
    - Implemented a text classification model using TensorFlow to automate email categorization, reducing manual tagging efforts across 150+ mailboxes.
    - Developed an XGBoost-based classification model to streamline client migration, reducing operational and maintenance costs.
    """)

    # Job 3: Mu Sigma
    st.subheader("Data Scientist - Mu Sigma")
    st.write("**Dec 2018 - Jan 2022**")
    st.write("""
    - Developed a Random Forest model to reduce unplanned machinery shutdowns for EGA, saving millions annually.
    - Built a Random Forest model to predict cash withdrawal demand, reducing Out-of-Cash scenarios across ATMs.
    """)

    # Skills Section
    st.header("Skills")
    st.write("""
    - **Machine Learning**: Linear Regression, Logistic Regression, SVM, KNN, Decision Tree, Random Forest, Ensemble Models
    - **Deep Learning**: Neural Networks, CNN, RNN, Attention, BERT, NLP, Computer Vision, Transformers
    - **Tools**: TensorFlow, Keras, Pandas, Numpy, Matplotlib, Seaborn, scikit-learn, ARIMA, Prophet, NLTK, OpenCV, YOLO V3, Databricks, Dataiku, Datarobot
    """)

    # Projects Section
    st.header("Hobby Projects")
    st.write("[**JusPy**: Personal ML Library | pip install juspy](https://pypi.org/project/juspy/)")
    st.write("[**Computer Vision Based Retail Store Analysis**](http://storeanalysiscv.jaspreetblogs.in)")

    # Education Section
    st.header("Education")
    st.write("**BITS Pilani** - M.Tech in AI & ML (2023 - 2025)")
    st.write("**LPU** - B.Tech in Computer Science (2014 - 2018)")