import streamlit as st
from project_pages.home import home
from project_pages.emoji_suggestion import emoji_suggestion
from project_pages.complaint_classification import complaint_classification


# Set the page configuration
st.set_page_config(
    page_title="Hobby Projects - Jaspreet",
    page_icon=":bar_chart:",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': 'mailto:ai.jaspreetsingh@gmail.com',
        'About': "This is a custom Streamlit app built for demonstration purposes by Jaspreet Singh. Visit linkedin.jaspreetblogs.in to get in touch."
    }
)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a Project", ["Home", "Emoji Suggestion", "Complaint Classification"])

# Page selection
if page == "Home":
    home()
elif page == "Emoji Suggestion":
    emoji_suggestion()
elif page == "Complaint Classification":
    complaint_classification()
