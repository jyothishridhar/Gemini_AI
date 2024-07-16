import streamlit as st
import google.generativeai as genai
import pandas as pd
import base64
import os
from openpyxl import Workbook
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

st.title("Generate Test Cases and Step Definitions")

requirement = st.text_area("Enter the requirements for generating test cases:")

if st.button("Generate Test Cases"):
    prompt = f"Generate BDD test cases and their respective step definitions for Selenium and Python based on the following requirements:\n\n{requirement}"
    response = get_gemini_response(prompt)
    
    st.subheader("Generated Test Cases and Step Definitions:")
    st.write(response)
    
    test_cases_list = [case.strip() for case in response.split('\n') if case.strip()]
    df = pd.DataFrame({"Test Cases and Step Definitions": test_cases_list})
    
    st.subheader("Generated Test Cases and Step Definitions (Formatted):")
    st.write(df)
    
    local_file_path = "C:\\Testcases\\test_cases_and_step_definitions.xlsx"
    directory = os.path.dirname(local_file_path)

    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        st.write(f"Directory created: {directory}")

    with pd.ExcelWriter(local_file_path, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']
    
    st.success(f"File saved successfully at {local_file_path}")

    st.download_button(
        label="Download data as Excel",
        data=open(local_file_path, 'rb'),
        file_name="test_cases_and_step_definitions.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    
    # Save the response to a separate Python script file
    script_file_path = "C:\\Testcases\\script.py"
    with open(script_file_path, 'w') as script_file:
        script_file.write(response)
    
    st.success(f"Script saved successfully at {script_file_path}")
    
    st.download_button(
        label="Download script as Python file",
        data=open(script_file_path, 'rb'),
        file_name="script.py",
        mime="text/x-python"
    )
