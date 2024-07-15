import streamlit as st
import google.generativeai as genai
import pandas as pd
import base64
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

# Function to generate Selenium script for a test case
def generate_selenium_script(test_case):
    script = f"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_case(self):
        driver = self.driver
        # Write your Selenium code here
        {test_case}

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
"""
    return script

st.title("Generate Test Cases and Automated Scripts")

requirement = st.text_area("Enter the requirements for generating test cases:")

if st.button("Generate Test Cases"):
    test_cases = get_gemini_response(requirement)
    
    st.subheader("Generated Test Cases:")
    st.write(test_cases)
    
    test_cases_list = [case.strip() for case in test_cases.split('\n') if case.strip()]
    df = pd.DataFrame({"Test Cases": test_cases_list})
    
    st.subheader("Generated Test Cases (Formatted):")
    st.write(df)

    local_file_path = "C:\\Testcases\\data.xlsx"
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
        file_name="data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    # Generate Selenium scripts
    selenium_scripts = [generate_selenium_script(case) for case in test_cases_list]
    
    st.subheader("Generated Selenium Scripts:")
    for script in selenium_scripts:
        st.code(script, language='python')
    
    # Save Selenium scripts to a file
    scripts_file_path = "C:\\Testcases\\selenium_scripts.py"
    with open(scripts_file_path, 'w') as f:
        for script in selenium_scripts:
            f.write(script + "\n\n")
    
    st.success(f"Selenium scripts saved successfully at {scripts_file_path}")
    
    # Allow users to download the Selenium scripts
    st.download_button(
        label="Download Selenium Scripts",
        data=open(scripts_file_path, 'rb'),
        file_name="selenium_scripts.py",
        mime="text/x-python"
    )
