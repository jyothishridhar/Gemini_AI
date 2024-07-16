from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


driver=None

@given('I am on the Paycomonline homepage')
def open_homepage():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.paycomonline.net/v4/ats/web.php/jobs?clientkey=FC9962A89833ED19DB7F75E9F964ACB9")

@when('I enter "Kennel assistant" in the search bar')
def search_kennel_assistant():
    global driver
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'quick-search'))
    )
    search_box.send_keys('Kennel assistant')
    
@then('I should see a list of jobs related to Kennel assistant')
def verify_results():
    global driver
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME,'jobTitle'))
    )    
    for result in results:
        assert 'Kennel assistant' in result.text


try:
    open_homepage()
    search_kennel_assistant()
    verify_results()
finally:
    driver.quit()        