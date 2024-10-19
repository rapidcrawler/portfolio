import streamlit as st
import nbformat

def campaign_analytics():
    st.title("Campaign Analytics")
    
    # Load the notebook content
    notebook_path = "./project_pages/model_campaign.ipynb"
    
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

    
    st.markdown("---")
    st.write("[Code Notebook](https://github.com/rapidcrawler/portfolio/blob/main/project_pages/campaign_analytics.py)")
    
    
