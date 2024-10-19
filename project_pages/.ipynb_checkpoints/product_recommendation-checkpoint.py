import streamlit as st
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import nbformat

def product_recommendation():
    st.title("Product Recommender 🛍️")
    # Step 1: Define product descriptions
    descriptions = [
        "This is a red cotton shirt with long sleeves",
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
    if 'clicked_product' not in st.session_state:
        st.session_state.clicked_product = None
    
    # Step 6: Show product selection radio button    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Choose a product")
        clicked_product = st.radio("", descriptions)
    
    with col2:
        st.subheader("Similar products:")
        
        if clicked_product:    
            # This variable holds the index of the product that the user selected or clicked
            clicked_product_idx = descriptions.index(clicked_product)
            # st.write(clicked_product_idx)
            
            # Vector representation of the product that the user clicked on
            query_vector = product_vectors[clicked_product_idx]
            # product_vectors = These array of numerical vectors are generated by the Sentence-BERT model and are used to represent the semantic meaning of 
            # each product description in a high-dimensional space
        
            # Perform the search for similar products
            k = 5  # This sets the number of similar products (nearest neighbors) that you want to retrieve
            # In this case, k = 5 means that the search will return the top 5 most similar products to the query product
            distances, indices = index.search(np.array([query_vector]), k)
            # index.search(): This function performs the similarity search using the FAISS index
            # distance: Euclidean distance between the query vector and the top k most similar vectors
            # indices: positions of the most similar products in the descriptions list
        
            # Display similar products
            similar_products = [descriptions[i] for i in indices[0]]
            for product in similar_products:
                st.write(f"**{product}**")
            
            # Add reset option
            if st.button("Reset"):
                st.session_state.clicked_product = None

    st.markdown("---")
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
