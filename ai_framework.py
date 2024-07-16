import streamlit as st
import google.generativeai as genai

# Configure API key
api_key = "AIzaSyAxz3eWwhOlP-g3Cws-O153RGnxoidGv_0"
genai.configure(api_key=api_key)

# Function to load Google Gemini Pro and get response
def get_gemini_response(prompt):
    model = genai.GenerativeModel('Gemini 1.5 Pro')
    response = model.generate_content([prompt])
    if not response or not response.parts:
        st.error("No valid response returned. The content might have been blocked.")
        return "No valid response returned. Please check the input requirements."
    return response.parts[0].text

# Function to generate BDD test cases and step definitions
def generate_bdd_test_cases(requirement):
    prompt = f"Generate BDD test cases and their respective step definitions for Selenium and Python based on the following requirements:\n\n{requirement}"
    response = get_gemini_response(prompt)
    return response

# Function to generate complete Python script from BDD test cases
def generate_complete_python_script(test_cases):
    test_cases_list = [case.strip() for case in test_cases.split('\n') if case.strip()]
    python_code = ""

    scenario_count = 0
    scenario_code = ""

    for case in test_cases_list:
        if case.startswith("Scenario"):
            if scenario_code:
                python_code += scenario_code + "\n\n"
            scenario_count += 1
            scenario_code = f"# {case}\ndef test_scenario_{scenario_count}():\n"
        elif case.startswith("* Given"):
            scenario_code += f"    # {case}\n"
            scenario_code += f"    # Implement your code here\n"
        elif case.startswith("* When"):
            scenario_code += f"    # {case}\n"
            scenario_code += f"    # Implement your code here\n"
        elif case.startswith("* Then"):
            scenario_code += f"    # {case}\n"
            scenario_code += f"    # Implement your code here\n"
    
    if scenario_code:
        python_code += scenario_code + "\n"
    
    return python_code

# Function to write Python script to file
def write_python_script_to_file(file_path, python_code):
    try:
        with open(file_path, 'w') as file:
            file.write(python_code)
        return True
    except Exception as e:
        st.error(f"Error occurred while saving Python script: {e}")
        return False

st.title("Generate Test Cases and Step Definitions")

requirement = st.text_area("Enter the requirements for generating test cases:")

if st.button("Generate Test Cases"):
    test_cases = generate_bdd_test_cases(requirement)
    
    st.subheader("Generated Test Cases and Step Definitions:")
    st.write(test_cases)

    python_code = generate_complete_python_script(test_cases)
    
    # Display generated Python script
    st.subheader("Generated Python Test Scripts:")
    st.text(python_code)

    # Save Python script to file
    file_name = "C:\\Testcases\\test_script.py"
    file_saved = write_python_script_to_file(file_name, python_code)
    
    if file_saved:
        st.success(f"Python script saved to: {file_name}")
    else:
        st.error("Failed to save Python script. Please check the logs for details.")
