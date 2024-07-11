import streamlit as st
import google.generativeai as genai
import pandas as pd
import base64
from io import BytesIO
import os
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font
from openpyxl.utils.dataframe import dataframe_to_rows

# Configure API key
api_key = "AIzaSyAxz3eWwhOlP-g3Cws-O153RGnxoidGv_0"
genai.configure(api_key=api_key)

# Function to load Google Gemini Pro and get response
def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt])
    if not response or not response.parts:
        st.error("No valid response returned. The content might have been blocked.")
        return "No valid response returned. Please check the input requirements."
    return response.parts[0].text

# Streamlit UI
st.title("Generate Test Cases")

# Input for user requirements
requirement = st.text_area("Enter the requirements for generating test cases:")

# Generate test cases based on user input
if st.button("Generate Test Cases"):
    test_cases = get_gemini_response(requirement)

    # Display the generated test cases
    st.subheader("Generated Test Cases:")
    st.write(test_cases)

    # Convert to DataFrame with each test case in a separate row
    test_cases_list = [case.strip() for case in test_cases.split('\n') if case.strip()]
    df = pd.DataFrame({"Test Cases": test_cases_list})

    # Display the DataFrame
    st.subheader("Generated Test Cases (Formatted):")
    st.write(df)

    local_file_path = "C:\\Testcases\\data.xlsx"
    directory = os.path.dirname(local_file_path)

    
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        st.write(f"Directory created: {directory}")

    # Save DataFrame to local Excel file
    with pd.ExcelWriter(local_file_path, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

    st.success(f"File saved successfully at {local_file_path}")

    # Provide download button for the Excel file
    st.download_button(
        label="Download data as Excel",
        data=open(local_file_path, 'rb'),
        file_name="data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
