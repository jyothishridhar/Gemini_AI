import streamlit as st
import google.generativeai as genai
import pandas as pd
import os
import ast

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

# Function to check syntax validity and return errors
def check_syntax(code):
    try:
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, e

# Function to check syntax validity line-by-line
def check_syntax_line_by_line(code):
    lines = code.split('\n')
    for i, line in enumerate(lines):
        is_valid, error = check_syntax(line)
        if not is_valid:
            return False, f"Line {i + 1}: {line} -> {error}"
    return True, None

# Function to clean the generated response
def clean_generated_response(response):
    lines = response.split('\n')
    cleaned_lines = []
    for line in lines:
        if line.strip().startswith("#") or not line.strip():  # Comment or empty line
            cleaned_lines.append(line)
        else:
            try:
                ast.parse(line)
                cleaned_lines.append(line)
            except SyntaxError:
                continue  # Skip invalid lines
    return "\n".join(cleaned_lines)

st.title("Generate Test Cases and Step Definitions")

requirement = st.text_area("Enter the requirements for generating test cases:")

if st.button("Generate Test Cases"):
    prompt = f"Generate BDD test cases and their respective step definitions for Selenium and Python based on the following requirements:\n\n{requirement}"
    response = get_gemini_response(prompt)
    
    # Debugging: Print the raw response
    st.subheader("Raw Response")
    st.write(response)
    
    st.subheader("Generated Test Cases and Step Definitions:")
    st.write(response)
    
    cleaned_response = clean_generated_response(response)
    
    # Debugging: Print the cleaned response
    st.subheader("Cleaned Response")
    st.write(cleaned_response)
    
    test_cases_list = [case.strip() for case in cleaned_response.split('\n') if case.strip()]
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

    # Line-by-line validation step
    is_valid, error = check_syntax_line_by_line(cleaned_response)
    if is_valid:
        st.success("Generated script is syntactically correct.")
    else:
        st.error(f"Generated script has syntax errors: {error}")

        # Display error details
        st.text_area("Error Details", error, height=200)
    
    # Save cleaned script to a .py file
    script_file_path = "C:\\Testcases\\generated_script.py"
    with open(script_file_path, "w") as file:
        file.write(cleaned_response)
    
    st.download_button(
        label="Download script as .py",
        data=open(script_file_path, 'rb'),
        file_name="generated_script.py",
        mime="text/x-python"
    )
