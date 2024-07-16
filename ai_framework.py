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

# Function to generate Python code from BDD test cases
def generate_python_code(requirement):
    prompt = f"Generate BDD test cases and their respective step definitions for Selenium and Python based on the following requirements:\n\n{requirement}"
    response = get_gemini_response(prompt)
    
    test_cases_list = [case.strip() for case in response.split('\n') if case.strip()]
    python_code = ""
    
    for index, case in enumerate(test_cases_list):
        if case.startswith("Scenario"):
            python_code += f"\n# {case}\n"
            python_code += f"def test_scenario_{index + 1}():\n"
        elif case.startswith("* Given"):
            python_code += f"    # {case}\n"
            python_code += f"    # Implement your code here\n"
        elif case.startswith("* When"):
            python_code += f"    # {case}\n"
            python_code += f"    # Implement your code here\n"
        elif case.startswith("* Then"):
            python_code += f"    # {case}\n"
            python_code += f"    # Implement your code here\n"
        python_code += "\n"
    
    return python_code

st.title("Generate Test Cases and Step Definitions")

requirement = st.text_area("Enter the requirements for generating test cases:")

if st.button("Generate Test Cases"):
    python_code = generate_python_code(requirement)
    
    st.subheader("Generated Python Test Scripts:")
    st.code(python_code, language='python')

    # Optionally, save to Excel
    # df = pd.DataFrame({"Test Cases and Step Definitions": test_cases_list})
    # ...
