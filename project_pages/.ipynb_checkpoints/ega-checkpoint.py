import streamlit as st
from PIL import Image

def ega():
    st.title('Unplanned Halts🛠️')    
    # Load your images
    image_1 = 'https://raw.githubusercontent.com/rapidcrawler/portfolio/refs/heads/main/imgs/EGA_Plant_%20(4).png'
    image_2 = 'https://raw.githubusercontent.com/rapidcrawler/portfolio/refs/heads/main/imgs/EGA_Plant_%20(2).png'
    image_3 = 'https://raw.githubusercontent.com/rapidcrawler/portfolio/refs/heads/main/imgs/EGA_Plant_%20(3).png'
    image_4 = 'https://raw.githubusercontent.com/rapidcrawler/portfolio/refs/heads/main/imgs/EGA_Plant_%20(5).png'
    image_5 = "https://raw.githubusercontent.com/rapidcrawler/portfolio/refs/heads/main/imgs/EGA_Plant_%20(7).png"
    
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
    
    st.image(image_5, caption='Manual Inspections', use_column_width=True)