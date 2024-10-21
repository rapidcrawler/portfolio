import streamlit as st
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import random
import nbformat

def product_recommendation():
    st.title("Product Recommender 🛍️")
    selected_product_index = None 
    # Step 1: Define product descriptions
    descriptions = [
        "A red cotton shirt with long sleeves",
        "Blue denim jeans with slim fit design",
        "Comfortable leather shoes in black color",
        "Casual t-shirt with cool graphic print",
        "Soft silk scarf with a floral pattern",
        "Lightweight running shoes with cushioned sole",
        "Elegant black dress with lace details",
        "Woolen winter coat with hood",
        "Leather handbag with gold accents",
        "Wireless noise-cancelling headphones",
        "Bluetooth speaker with deep bass",
        "Smartphone with 128GB storage and dual camera",
        "Smartwatch with fitness tracking features",
        "Laptop with 16GB RAM and Intel i7 processor",
        "Tablet with 10-inch display and stylus support",
        "Ergonomic office chair with lumbar support",
        "Standing desk with adjustable height",
        "LED desk lamp with adjustable brightness",
        "Portable hard drive with 2TB storage",
        "Wireless gaming mouse with RGB lighting"
    ]

    product_images = [
        "https://printmytee.in/wp-content/uploads/2021/07/Product-Your-Design-Here-06.jpg",
        "https://www.vudu.co.in/cdn/shop/files/VibrantBlueDenim-VUDU1.jpg?v=1723135422&width=1080",
        "https://5.imimg.com/data5/SELLER/Default/2023/10/351833578/DV/GA/TH/24966853/leather-formal-2-01-01-500x500.jpg",
        "https://veirdo.in/cdn/shop/files/Artboard8.png?v=1724158576",
        "https://m.media-amazon.com/images/I/61BMBWFk6NL._AC_UF894,1000_QL80_.jpg",
        "https://static.nike.com/a/images/t_PDP_936_v1/f_auto,q_auto:eco/ca929f7e-f433-46b7-8d83-1a6171c172ce/NIKE+REVOLUTION+7+EASYON.png",
        "https://i.pinimg.com/736x/85/c2/b4/85c2b440f1c1912cd26269a84867d3e2.jpg",
        "https://image.made-in-china.com/202f0j00WtFqUgkPaicI/Winter-Men-s-Jacket-Woolen-Coat-MID-Length-All-Match-Casual-Woolen-Men-s-Coat-Thickened-Cross-Border-Woolen-Coat-Men.webp",
        "https://m.media-amazon.com/images/I/51-+SFrhYFL._AC_UY1000_.jpg",
        "https://www.dealsplant.com/cdn/shop/products/dealsplant-headphones-earphones-logitech-h111-wired-headphones-with-mic-single-3-5-mm-audio-jack-pc-mac-laptop-smartphone-tablet-15790096416843.jpg?v=1660051238",
        "https://cdn.thewirecutter.com/wp-content/media/2024/07/portablebluetoothspeakers-2048px-3321-2x1-1.jpg?width=2048&quality=75&crop=2:1&auto=webp",
        "https://www.techadvisor.com/wp-content/uploads/2024/10/best-phones-2024-3.jpg?quality=50&strip=all",
        "https://cdn.mos.cms.futurecdn.net/FkGweMeB7hdPgaSFQdgsfj-1200-80.jpg",
        "https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RW16TLT?ver=99ac&q=90&m=6&h=705&w=1253&b=%23FFFFFFFF&f=jpg&o=f&p=140&aim=true",
        "https://media.wired.com/photos/649b2dbfc859c4a1cdecc412/master/w_320%2Cc_limit/Amazon-Fire-Max-11-Review--Stand-Gear.jpg",
        "https://www.chennaichairs.com/images/thumbs/0006313_ample-mesh-office-chair_625.webp",
        "https://www.vari.com/on/demandware.static/-/Library-Sites-VariGlobalContentLibrary/default/dw4fc82d3e/sub-cat-banner/standing-desks-clp.jpg",
        "https://rukminim1.flixcart.com/image/300/300/xif0q/table-lamp/1/i/3/desk-lamp-for-study-with-3-shades-touch-control-light-and-mobile-original-imagudcf3ajntsgs.jpeg",
        "https://www.securedatarecovery.com/media/services/hard-drive-recovery-video.webp",
        "https://www.jiomart.com/images/product/original/rvh3q3dfsc/gaming-mouse-with-6-buttons-wired-optical-mouse-with-rgb-lights-for-laptops-desktop-computer-product-images-orvh3q3dfsc-p595275392-0-202211121918.jpg?im=Resize=(420,420)"
    ]
    
    # Step 2: Load Sentence-BERT model for vectorization
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Step 3: Convert product descriptions to vectors
    product_vectors = model.encode(descriptions)
    # This step converts textual product descriptions into numerical vectors using a pre-trained model
    # In this case, the model is a Sentence-BERT model (which was initialized earlier with SentenceTransformer('all-MiniLM-L6-v2'))
    
    # Sentence-BERT is a variant of the BERT model that is fine-tuned to generate embeddings for sentences or texts
    # It transforms each product description into a fixed-size vector that captures the semantic meaning of the sentence

    # The result (product_vectors) is a list of vectors, one for each product description
    # Each vector represents the meaning of the corresponding product description in a high-dimensional space
    
    # Step 4: Normalize vectors (FAISS recommends normalizing vectors)
    product_vectors = np.array([vec / np.linalg.norm(vec) for vec in product_vectors])
    # This step normalizes the vectors to ensure they all have unit length (i.e., their magnitude or length is 1)
    # This is recommended for similarity searches to ensure that the comparison focuses only on the direction of the vectors, not their magnitude
    
    # Step 5: Create FAISS index
    d = product_vectors.shape[1]  # get dimension of the vector embeddings
    index = faiss.IndexFlatL2(d)   # FAISS will use this to compute L2 Eucledian distance between vectors during the search process
    index.add(product_vectors)     # adds the normalized product vectors to the FAISS index. After this, the index is ready for performing similarity searches
    # FAISS is being used here to efficiently perform nearest-neighbor search based on vector similarity
    # This step initializes a FAISS index using Euclidean distance (L2) to measure similarity between vectors
    
    # Initialize session state
    
    # if 'clicked_product' not in st.session_state:
    #     st.session_state.clicked_product = None
    selected_product_index = 0
    # Step 6: Show product selection radio button    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Choose a product")
        # clicked_product = st.radio("", descriptions)
        for i, description in enumerate(descriptions):
            # Create a new column for each product (image and description side by side)
            cols = st.columns([1, 2])  # Image on left (1 part), description on right (2 parts)
            
            # Display product image in the first column
            with cols[0]:
                st.image(product_images[i], width=100)
            
            # Display product description and a button in the second column
            with cols[1]:
                st.write(description)
                if st.button(f"Select", key=f"button_{i}"):
                    selected_product_index = i
        
        # Step 4: Display the selected product
        clicked_product = descriptions[selected_product_index]
    
    with col2:
        st.subheader("Similar products:")
        max_prod_recco = st.slider('Similar Products To Recommend:', min_value=3, max_value=6, value=4)
        # This sets the number of similar products (nearest neighbors) that you want to retrieve
        
        if clicked_product:    
            # This variable holds the index of the product that the user selected or clicked
            clicked_product_idx = descriptions.index(clicked_product)
            # st.write(clicked_product_idx)
            
            # Vector representation of the product that the user clicked on
            query_vector = product_vectors[clicked_product_idx]
            # product_vectors = These array of numerical vectors are generated by the Sentence-BERT model and are used to represent the semantic meaning of 
            # each product description in a high-dimensional space
        
            # Perform the search for similar products
            # In this case, k = 5 means that the search will return the top 5 most similar products to the query product
            distances, indices = index.search(np.array([query_vector]), max_prod_recco+1)
            # index.search(): This function performs the similarity search using the FAISS index
            # distance: Euclidean distance between the query vector and the top k most similar vectors
            # indices: positions of the most similar products in the descriptions list
        
            # Display similar products
            st.write(f"Chosen Product:\n{clicked_product}")
            cols = st.columns([1, 2])  # Image on left (1 part), description on right (2 parts)      
            with cols[0]:
                 st.image(product_images[descriptions.index(clicked_product)], width=100)
            with cols[1]:
                st.write(f"**{clicked_product}**")
            st.divider()
            
            st.write(f"Displaying {max_prod_recco} Suggestions")
            
            similar_products = [descriptions[i] for i in indices[0]]

            cols = st.columns([1, 2])  # Image on left (1 part), description on right (2 parts)            
            # Skipping index 0, as index 0 is always the same text, that's being searched due to highest similarity with itself 
            for idx, product in enumerate(similar_products[1:], start=1):                
                # Display product image in the first column
                with cols[0]:
                    st.image(product_images[descriptions.index(product)], width=100)
                # Display product description and a button in the second column
                with cols[1]:                
                        st.write(f"**{idx}: {product}**")                
                    

            
            # Add reset option
            if st.button("Reset"):
                st.session_state.clicked_product = None

    st.divider()
    st.caption(":loudspeaker: :blue[Future Updates] :loudspeaker:")
    st.caption(
        """
        1. __Technical Upgrade__: Using BERT's Word-Embedding for context aware transformation of words in product descriptions
        2. __Technical Upgrade__: Using image object detection for missing description in product listings
        3. __Cosmetic Changes__: Displaying product images along with description
        """
    )
    st.divider()
    
    st.divider()
    st.write("[Code Notebook](https://github.com/rapidcrawler/portfolio/blob/main/project_pages/product_recommendation.py)")

    # Load the notebook content
    notebook_path = "./project_pages/model_product_reco.ipynb"

    # Read the notebook
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook_content = nbformat.read(f, as_version=4)
    
    # Display the notebook content with outputs
    for cell in notebook_content.cells:
        if cell.cell_type == "markdown":
            # Display markdown cells
            st.markdown(cell.source)
        elif cell.cell_type == "code":
            # Display code cells
            st.code(cell.source)
    
            # Display outputs if available
            if 'outputs' in cell:
                for output in cell['outputs']:
                    if output['output_type'] == 'execute_result':
                        # Display plain text outputs
                        if 'text/plain' in output['data']:
                            st.text(output['data']['text/plain'])
                    
                    elif output['output_type'] == 'stream':
                        # Display streamed output like print statements
                        st.text(output['text'])
                    
                    elif output['output_type'] == 'error':
                        # Display error messages
                        st.error(''.join(output['traceback']))
    
                    elif output['output_type'] == 'display_data':
                        # Display HTML or rich outputs
                        if 'text/html' in output['data']:
                            st.write(output['data']['text/html'], unsafe_allow_html=True)
