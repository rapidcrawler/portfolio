import streamlit as st
from project_pages.home import home
from project_pages.emoji_suggestion import emoji_suggestion
from project_pages.complaint_classification import complaint_classification
from project_pages.smart_store import smart_store
from project_pages.email_clf import email_clf
from project_pages.campaign_analytics import campaign_analytics


# Set the page configuration
st.set_page_config(
    page_title="Hobby Projects - Jaspreet",
    page_icon=":briefcase:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': 'mailto:ai.jaspreetsingh@gmail.com',
        'About': "This is a custom Streamlit app built for demonstration purposes by Jaspreet Singh. Visit linkedin.jaspreetblogs.in to get in touch."
    }
)

# Sidebar for navigation
st.sidebar.title("Navigation")
project_list = [
    "Home",  "Smart Stores", "Emoji Suggestion", "Complaint Classification"
    , "Campaign Analytics", "eMail Classifier"
]
page = st.sidebar.selectbox("Choose a Project", project_list)

# Page selection
if page == "Home":
    home()
elif page == project_list[1]:
    smart_store()
elif page == project_list[2]:
    emoji_suggestion()
elif page == project_list[3]:
    complaint_classification()
elif page == project_list[4]:
    campaign_analytics()
elif page == project_list[5]:
    email_clf()
    
    
