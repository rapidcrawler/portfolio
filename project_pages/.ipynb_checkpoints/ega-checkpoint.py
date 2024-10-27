import streamlit as st
from PIL import Image

def ega():
    st.title('Unplanned Halts🛠️')
    st.caption(
         """
         1) Emirates Global Aluminum (EGA) was facing multiple frequent production halts due to machinery faults which would last for more than weeks and cost multiple millions dollar in loss of opportunity
         
         2) Assisted EGA to reduce unplanned maintenance shutdown, production halts and improve equipment life cycle by predicting potential machinery failures well in advance
         
         3) Proposed Random Forest based predictive solution lead to operational savings of over millions annually in production deferral costs 
         """
    )

    # Load your images
    image_1 = 'https://raw.githubusercontent.com/rapidcrawler/portfolio/refs/heads/main/imgs/EGA_Plant_%20(4).png'
    image_2 = 'https://raw.githubusercontent.com/rapidcrawler/portfolio/refs/heads/main/imgs/EGA_Plant_%20(2).png'
    image_3 = 'https://raw.githubusercontent.com/rapidcrawler/portfolio/refs/heads/main/imgs/EGA_Plant_%20(3).png'
    image_4 = 'https://raw.githubusercontent.com/rapidcrawler/portfolio/refs/heads/main/imgs/EGA_Plant_%20(5).png'
    image_5 = "https://raw.githubusercontent.com/rapidcrawler/portfolio/refs/heads/main/imgs/EGA_Plant_%20(7).png"
    image_6 = "https://raw.githubusercontent.com/rapidcrawler/portfolio/refs/heads/main/imgs/EGA_Plant_%20(6).png"
    
    # Display images in a 2 by 2 layout using columns
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    
    with col1:
        st.image(image_1, caption='Smelting Plant', use_column_width=True)
        
    with col2:
        st.image(image_2, caption='Cathodes', use_column_width=True)
        
    with col3:
        st.image(image_3, caption='Detoriated Cathodes', use_column_width=True)
        
    with col4:
        st.image(image_4, caption='Manual Inspections', use_column_width=True)
    
    st.divider()
    st.subheader("Results")
    col5, col6 = st.columns(2)
    with col5:
        st.image(image_5, caption='Solution Outcome', use_column_width=True)
        st.write("Via: Predicting Risk-to-Failure in hourly basis for efficient pro-active maintenance")
    with col6:
        st.image(image_6, caption='Monthly Monitoring', use_column_width=True)
        st.write("Via: Avoiding Overuse & Energy-Efficient Shutdowns and Automating Cathode Health Chekups")

    # Add a divider and section for IoT Sensors at the end
    st.divider()
    st.subheader("IoT Sensors Used in Aluminum Production")

    # Temperature Sensors
    st.write("**Temperature Sensors**")
    st.write("""
    - Furnace temperature
    - Cooling temperature
    - Anode/cathode temperature
    """)

    # Pressure Sensors
    st.write("**Pressure Sensors**")
    st.write("""
    - Pressure in the furnace
    - Casting molds pressure
    - Pipeline pressure
    """)

    # Gas Sensors
    st.write("**Gas Sensors**")
    st.write("""
    - CO2, NOx, SO2 emission levels
    """)

    # Humidity Sensors
    st.write("**Humidity Sensors**")
    st.write("""
    - Humidity levels in production and storage areas
    """)
    
    # Dependent Variable
    st.write("**Dependent Variable**")
    st.write("""
    - Smelter Shutdown
    """)


