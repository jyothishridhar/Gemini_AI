# import streamlit as st
# import google.generativeai as genai
# import os

# # Configure API key
# api_key = "AIzaSyAxz3eWwhOlP-g3Cws-O153RGnxoidGv_0"
# genai.configure(api_key=api_key)

# # Function to load Google Gemini Pro and get response
# def get_gemini_response(prompt):
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content([prompt])
#     if not response or not response.parts:
#         st.error("No valid response returned. The content might have been blocked.")
#         return "No valid response returned. Please check the input requirements."
#     return response.parts[0].text

# # Function to generate BDD test cases and step definitions
# def generate_bdd_test_cases(requirement):
#     prompt = f"Generate BDD test cases and their respective step definitions for Selenium and Python based on the following requirements:\n\n{requirement}"
#     response = get_gemini_response(prompt)
#     return response

# # Function to generate complete Python script from BDD test cases
# def generate_complete_python_script(test_cases):
#     test_cases_list = [case.strip() for case in test_cases.split('\n') if case.strip()]
#     python_code = ""

#     scenario_count = 0
#     scenario_code = ""

#     for case in test_cases_list:
#         if case.startswith("Scenario"):
#             if scenario_code:
#                 python_code += scenario_code + "\n\n"
#             scenario_count += 1
#             scenario_code = f"# {case}\ndef test_scenario_{scenario_count}():\n"
#         elif case.startswith("* Given"):
#             scenario_code += f"    # {case}\n"
#             scenario_code += f"    # Implement your code here\n"
#         elif case.startswith("* When"):
#             scenario_code += f"    # {case}\n"
#             scenario_code += f"    # Implement your code here\n"
#         elif case.startswith("* Then"):
#             scenario_code += f"    # {case}\n"
#             scenario_code += f"    # Implement your code here\n"
    
#     if scenario_code:
#         python_code += scenario_code + "\n"
    
#     return python_code

# # Function to write Python script to file
# def write_python_script_to_file(file_path, python_code):
#     try:
#         with open(file_path, 'w') as file:
#             file.write(python_code)
#         return True
#     except Exception as e:
#         st.error(f"Error occurred while saving Python script: {e}")
#         return False

# st.title("Generate Test Cases and Step Definitions")

# requirement = st.text_area("Enter the requirements for generating test cases:")

# if st.button("Generate Test Cases"):
#     test_cases = generate_bdd_test_cases(requirement)
    
#     st.subheader("Generated Test Cases and Step Definitions:")
#     st.write(test_cases)

#     python_code = generate_complete_python_script(test_cases)
    
#     # Display generated Python script
#     st.subheader("Generated Python Test Scripts:")
#     st.text(python_code)

#     # Save Python script to file
#     features_directory = "C:\\AI_framework\\features"
#     automated_py_file = "C:\\AI_framework\\Automated_script.py"
    
#     if not os.path.exists(features_directory):
#         os.makedirs(features_directory)
    
#     file_saved_features = write_python_script_to_file(os.path.join(features_directory, "test_cases.feature"), test_cases)
#     file_saved_automated_py = write_python_script_to_file(automated_py_file, python_code)
    
#     if file_saved_features and file_saved_automated_py:
#         st.success(f"Test cases saved to: {features_directory}\\test_cases.feature")
#         st.success(f"Python script saved to: {automated_py_file}")
#     else:
#         st.error("Failed to save test cases or Python script. Please check the logs for details.")


# import streamlit as st
# import google.generativeai as genai
# import os

# # Configure API key
# api_key = "AIzaSyAxz3eWwhOlP-g3Cws-O153RGnxoidGv_0"
# genai.configure(api_key=api_key)

# # Define features directory globally
# features_directory = "C:\\AI_framework\\features"

# # Function to load Google Gemini Pro and get response
# def get_gemini_response(prompt):
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content([prompt])
#     if not response or not response.parts:
#         st.error("No valid response returned. The content might have been blocked.")
#         return "No valid response returned. Please check the input requirements."
#     return response.parts[0].text

# # Function to generate BDD test cases
# def generate_bdd_test_cases(requirement):
#     prompt = f"Generate BDD test cases based on the following requirements:\n\n{requirement}"
#     response = get_gemini_response(prompt)
#     return response

# # Function to generate complete Python script from BDD test cases
# def generate_complete_python_script(test_cases):
#     prompt = f"Generate Python code with step definitions for the following BDD test cases:\n\n{test_cases}"
#     response = get_gemini_response(prompt)
#     return response

# # Function to write to file
# def write_to_file(file_path, content):
#     try:
#         with open(file_path, 'w') as file:
#             file.write(content)
#         return True
#     except Exception as e:
#         st.error(f"Error occurred while saving to file: {e}")
#         return False

# # Streamlit interface
# st.title("BDD Test Case Generator")

# # Step 1: Input requirements and generate BDD test cases
# requirement = st.text_area("Enter the requirements for generating test cases:")

# if st.button("Generate BDD Test Cases"):
#     test_cases = generate_bdd_test_cases(requirement)
    
#     # Display only the BDD test cases
#     st.subheader("Generated BDD Test Cases:")
#     st.write(test_cases)
    
#     # Ensure directory exists
#     if not os.path.exists(features_directory):
#         os.makedirs(features_directory)
    
#     # Save the test cases to a file
#     test_case_file_path = os.path.join(features_directory, "test_cases.feature")
#     file_saved_features = write_to_file(test_case_file_path, test_cases)
    
#     if file_saved_features:
#         st.success(f"Test cases saved to: {test_case_file_path}")
#     else:
#         st.error("Failed to save test cases. Please check the logs for details.")

# # Step 2: Select a stored test cases file and generate script
# st.subheader("Generate Python Script from Stored Test Cases")

# # List the files in the features directory
# if os.path.exists(features_directory):
#     test_case_files = [f for f in os.listdir(features_directory) if f.endswith(".feature")]
# else:
#     test_case_files = []

# selected_file = st.selectbox("Select a test cases file:", test_case_files)

# if selected_file:
#     selected_file_path = os.path.join(features_directory, selected_file)
#     with open(selected_file_path, 'r') as file:
#         stored_test_cases = file.read()
    
#     st.text_area("Stored BDD Test Cases:", value=stored_test_cases, height=300)
    
#     if st.button("Generate Step Definitions and Python Script"):
#         st.write("Generating script...")
#         python_code = generate_complete_python_script(stored_test_cases)
        
#         st.subheader("Generated Python Test Scripts:")
#         st.text(python_code)
        
#         automated_py_file = "C:\\AI_framework\\Automated_script.py"
        
#         file_saved_py = write_to_file(automated_py_file, python_code)
        
#         if file_saved_py:
#             st.success(f"Python script saved to: {automated_py_file}")
#         else:
#             st.error("Failed to save Python script. Please check the logs for details.")


import streamlit as st
import google.generativeai as genai
import os
import pandas as pd

# Configure API key
api_key = "AIzaSyAxz3eWwhOlP-g3Cws-O153RGnxoidGv_0"
genai.configure(api_key=api_key)

# Define features directory globally
features_directory = "C:\\AI_framework\\features"

# Function to load Google Gemini Pro and get response
def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt])
    if not response or not response.parts:
        st.error("No valid response returned. The content might have been blocked.")
        return "No valid response returned. Please check the input requirements."
    return response.parts[0].text

# Function to generate BDD test cases
def generate_bdd_test_cases(requirement):
    prompt = f"Generate test cases based on the following requirements:\n\n{requirement}"
    response = get_gemini_response(prompt)
    return response

# Function to generate complete Python script from BDD test cases
def generate_complete_python_script(test_cases, script_requirements):
    prompt = f"""
    Please follow the below steps for script generation:
    {script_requirements}
    
    Generate code  for the following  test cases:
    \n\n{test_cases}
    """
    response = get_gemini_response(prompt)
    return response

# Function to write to file
def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return True
    except Exception as e:
        st.error(f"Error occurred while saving to file: {e}")
        return False

# Function to convert non-BDD text to BDD format
def convert_to_bdd_format(text):
    prompt = f"Convert the following text to BDD format:\n\n{text}"
    response = get_gemini_response(prompt)
    return response

# Function to process uploaded file
def process_uploaded_file(uploaded_file):
    if uploaded_file.name.endswith('.txt'):
        content = uploaded_file.read().decode("utf-8")
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
        content = df.to_string(index=False)
    else:
        st.error("Unsupported file format. Please upload a .txt or .xlsx file.")
        return None
    return content

# Streamlit interface
st.title("BDD Test Case Generator")

# Step 1: Input requirements and generate BDD test cases
requirement = st.text_area("Enter the requirements for generating test cases:")
# test_cases = st.text_area("Enter the requirement for script generation:")
script_requirements = st.text_area("Enter specific requirements for script generation:")

uploaded_file = st.file_uploader("Or upload a non-BDD formatted requirements file:", type=["txt", "xlsx"])

if st.button("Generate Test Cases"):
    if uploaded_file:
        content = process_uploaded_file(uploaded_file)
        if content:
            requirement = convert_to_bdd_format(content)
            st.text_area("Converted  Format Requirements:", value=requirement, height=300)
    
    if requirement:
        test_cases = generate_bdd_test_cases(requirement)
        
        # Display only the BDD test cases
        st.subheader("Generated Test Cases:")
        st.write(test_cases)
        
        # Ensure directory exists
        if not os.path.exists(features_directory):
            os.makedirs(features_directory)
        
        # Save the test cases to a file
        test_case_file_path = os.path.join(features_directory, "test_cases.feature")
        file_saved_features = write_to_file(test_case_file_path, test_cases)
        
        if file_saved_features:
            st.success(f"Test cases saved to: {test_case_file_path}")
        else:
            st.error("Failed to save test cases. Please check the logs for details.")

# Step 2: Select a stored test cases file and generate script
st.subheader("Generate Script from Stored Test Cases")

# List the files in the features directory
if os.path.exists(features_directory):
    test_case_files = [f for f in os.listdir(features_directory) if f.endswith(".feature")]
else:
    test_case_files = []

selected_file = st.selectbox("Select a test cases file:", test_case_files)

if selected_file:
    selected_file_path = os.path.join(features_directory, selected_file)
    with open(selected_file_path, 'r') as file:
        stored_test_cases = file.read()
    
    st.text_area("Stored  Test Cases:", value=stored_test_cases, height=300)
    
    if st.button("Generate Step Definitions"):
        if script_requirements:
            st.write("Generating script...")
            python_code = generate_complete_python_script(stored_test_cases, script_requirements)
            
            st.subheader("Generated Test Scripts:")
            st.text(python_code)
            
            automated_py_file = "C:\\AI_framework\\Automated_script.py"
            
            file_saved_py = write_to_file(automated_py_file, python_code)
            
            if file_saved_py:
                st.success(f"Script saved to: {automated_py_file}")
            else:
                st.error("Failed to save script. Please check the logs for details.")
