import streamlit as st

def smart_store():
    st.title("Smart Stores 🛒")
    
    # Create two columns for image and name/introduction
    col1, col2, col3 = st.columns([3,1,3])  # Adjust the width ratio as needed
    
    
    with col1:
        st.markdown(
        """
         <div style="text-align: justify;">
         <ul>
         <li>
             <u><strong>Situation</strong></u>: Understanding offline customer's behavior patterns to make better decisions in store operations (staff management, product placements, etc)
         </li>
        <li>
            <u><strong>Complication</strong></u>: Implemented in-store video analytics solution using Single shot multibox detector (SSD) based YOLO V3 solution
        </li>
        <li>
            <u><strong>Resolution</strong></u>: Delivered hour level data about customer entry, exit & in-store count, number of aisle visits, traditional checkout counter count, Scan-&-Go counters encouragement and others 
        </li>
        </div>
        """
        , unsafe_allow_html=True)

    
    with col2:
        st.write("")
        st.image("https://cdn-icons-png.flaticon.com/512/774/774181.png", width=150)
        
    with col3:
        st.markdown(
        """
         <div style="text-align: justify;">
         <ul>
         <li>
             <u><strong>Situation</strong></u>: Understanding offline customer's behavior patterns to make better decisions in store operations (staff management, product placements, etc)
         </li>
        <li>
            <u><strong>Complication</strong></u>: Implemented in-store video analytics solution using Single shot multibox detector (SSD) based YOLO V3 solution
        </li>
        <li>
            <u><strong>Resolution</strong></u>: Delivered hour level data about customer entry, exit & in-store count, number of aisle visits, traditional checkout counter count, Scan-&-Go counters encouragement and others 
        </li>
        </div>
        """
        , unsafe_allow_html=True)
    
    # Displaying Sample Video
    st.video("https://github.com/rapidcrawler/hobby_projects/raw/refs/heads/main/comp_vision_topics/02_Object_Detection_With_SSD/Motion_Tracker_00.mp4")
