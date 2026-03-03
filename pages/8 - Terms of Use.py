import pandas as pd
import streamlit as st
from pathlib import Path

# Function to read the content of a markdown file
def read_markdown_file(file_path):
    """Reads a markdown file and returns its content as a string."""
    try:
        # Use Pathlib to read the file content
        return Path(file_path).read_text()
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."

# Specify the path to your markdown file
markdown_file_path = "Terms-of-Use.md" # Replace with your file name/path

# Read the file content
intro_markdown = read_markdown_file(markdown_file_path)

# Display the markdown content in Streamlit
st.markdown(intro_markdown, unsafe_allow_html=True) # Set unsafe_allow_html=True if you need to render HTML within the markdown

# You can add other Streamlit elements below or above the markdown content
st.write("---") # Adds a horizontal divider



st.write("  ---------------------------------------------------------------  ")
# # ###################################################################
with st.container():
    f9, f10, f11 = st.columns([2, 5, 1])
    with f9:
        st.write(" ")
    with f10:
        st.write(": 2025 - 2026 | All Rights Reserved  ©  Ledgr Inc.")
        st.write(": alphaLedgr.com | alphaLedgr Technologies Ltd. :")
    with f11:
        st.write(" ")
