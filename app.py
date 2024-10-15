import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Hobby Projects - Jaspreet"
    , page_icon=":bar_chart:"
    , layout="centered", initial_sidebar_state="expanded"
    , menu_items={
        'Report a bug': 'mailto:ai.jaspreetsingh@gmail.com',  # This will open the default email camalient
        'About': "This is a custom Streamlit app built for demonstration purposes by Jaspreet Singh. Visit linkedin.jaspreetblogs.in to get in touch."
    })

# Define functions for each page
def home():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")
    st.image("https://d2jdgazzki9vjm.cloudfront.net/computer/images/what-is-a-home-page.jpg", caption="Home Page Image")  # Add your image path here

def about():
    st.title("Emoji Suggestion")
    st.write("This is the About Page.")
    st.image("https://www.tapsmart.com/wp-content/uploads/2016/08/emoji-messages-ios10-3.png", caption="About Page Image")  # Add your image path here

def contact():
    st.title("Complaint Classification")
    st.write("Get in touch with us on the Contact Page!")
    st.image("https://marketing-interactive-assets.b-cdn.net/images/sg/content-images/complaints.jpg", caption="Contact Page Image")  # Add your image path here

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a Project", ["Home", "Emoji Suggestion", "Complaint Classification"])

# Page selection
if page == "Home":
    home()
elif page == "Emoji Suggestion":
    about()
elif page == "Complaint Classification":
    contact()
