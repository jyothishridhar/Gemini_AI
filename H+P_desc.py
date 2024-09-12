

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

class Context:
    def __init__(self):
        self.driver = driver

context = Context()


BASE_URL = "https://www.paycomonline.net/v4/ats/web.php/jobs/ViewJobDetails?job=99510&clientkey=FC9962A89833ED19DB7F75E9F964ACB9"
driver.get(BASE_URL)


@given('the user is on the home page')
def open_marriott_website(context):
    driver.get(BASE_URL)


@given('the user clicks on a Job Title with a corresponding URL')
def click_on_job_title(context):
    try:
        job_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="results"]/li'))
        )
        job_title.click()
        print(f"PASS: Clicked on the job title successfully")
    except Exception as e:
        print(f"FAILED: Unable to click on the job title: {e}")


@then('the job description is displayed')
def verify_job_description(context):
    try:
        job_description = driver.find_element('xpath','//*[@id="jobDesc-row"]/div/span').get_attribute('outerHTML')
        print('Job_description',job_description)
        if job_description.is_displayed():
            print(f"PASS: Job description is displayed successfully")
        else:
            print(f"FAILED: Job description is not displayed")
    except Exception as e:
        print(f"FAILED: Unable to verify job description: {e}")
    finally:
        driver.quit()


try:
    open_marriott_website(context)
    click_on_job_title(context)
    verify_job_description(context)
finally:
    driver.quit()        