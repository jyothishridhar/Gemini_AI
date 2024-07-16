from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from behave import given, when, then


@given("User is on the Paycomonline homepage")
def step_1(context):
    try:
        context.browser = webdriver.Chrome()
        context.browser.get("https://www.paycomonline.net/v4/ats/web.php/jobs?clientkey=FC9962A89833ED19DB7F75E9F964ACB9")
    except:
        print("Error: Could not navigate to the Paycomonline homepage.")

@when("User clicks on \"Veterinary Care\" in the \"Job Category\" filter")
def step_2(context):
    try:
        job_category_filter = context.browser.find_element(By.ID, "jobCategory")
        veterinary_care_option = job_category_filter.find_element(By.XPATH, "//option[text()='Veterinary Care']")
        veterinary_care_option.click()
    except:
        print("Error: Could not select the \"Veterinary Care\" option in the \"Job Category\" filter.")

@when("User clicks on the 'Search' button")
def step_3(context):
    try:
        search_button = context.browser.find_element(By.ID, "searchButton")
        search_button.click()
    except:
        print("Error: Could not click on the 'Search' button.")

@then("The search results page should display jobs in the \"Veterinary Care\" category")
def step_4(context):
    try:
        time.sleep(3)
        jobs = context.browser.find_elements(By.CSS_SELECTOR, "div.result")
        for job in jobs:
            if "Veterinary Care" not in job.text:
                print("Error: The search results page does not contain jobs in the \"Veterinary Care\" category.")
                return False
        print("Success: The search results page displays jobs in the \"Veterinary Care\" category.")
        return True
    except:
        print("Error: Could not verify the search results page.")
    finally:
        context.browser.close()

if __name__ == "__main__":
    from behave import __main__ as behave_main
    behave_main.main(["-s"])  