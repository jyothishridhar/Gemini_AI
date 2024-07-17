from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
import time

driver = None

def report_step_result(step_name, result):
    print(f"{step_name}: {'PASSED' if result else 'FAILED'}")

@given('I am on the Paycomonline homepage')
def open_homepage():
    global driver
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.paycomonline.net/v4/ats/web.php/jobs?clientkey=FC9962A89833ED19DB7F75E9F964ACB9")
        report_step_result("Open Paycomonline homepage", True)
    except Exception as e:
        report_step_result("Open Paycomonline homepage", False)
        raise e

@when('I enter "Kennel assistant" in the search bar')
def search_kennel_assistant():
    global driver
    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'quick-search'))
        )
        search_box.send_keys('Kennel assistant')
        report_step_result('Enter "Kennel assistant" in the search bar', True)
    except Exception as e:
        report_step_result('Enter "Kennel assistant" in the search bar', False)
        raise e

@then('I should see a list of Kennel Assistant job URLs')
def then_i_should_see_a_list_of_kennel_assistant_job_urls():
    global driver
    try:
        time.sleep(5)
        results = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[@class="JobListing__container"]'))
        )
        urls = [result.get_attribute("href") for result in results]
        assert any("Kennel Assistant" in result.text for result in results), "No job listings found for 'Kennel Assistant'"
        report_step_result('See a list of Kennel Assistant job URLs', True)
        
        # Print all URLs
        for url in urls:
            print(url)
    except Exception as e:
        report_step_result('See a list of Kennel Assistant job URLs', False)
        raise e

try:
    open_homepage()
    search_kennel_assistant()
    then_i_should_see_a_list_of_kennel_assistant_job_urls()
finally:
    if driver:
        driver.quit()









# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from behave import given, when, then
# import time


# driver=None

# @given('I am on the Paycomonline homepage')
# def open_homepage():
#     global driver
#     driver = webdriver.Chrome()
#     driver.get("https://www.paycomonline.net/v4/ats/web.php/jobs?clientkey=FC9962A89833ED19DB7F75E9F964ACB9")

# @when('I enter "Kennel assistant" in the search bar')
# def search_kennel_assistant():
#     global driver
#     search_box = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, 'quick-search'))
#     )
#     search_box.send_keys('Kennel assistant')
    

# @then('I should see a list of Kennel Assistant job URLs')
# def then_i_should_see_a_list_of_kennel_assistant_job_urls():
#     global driver
#     time.sleep(5)
#     results = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located((By.XPATH, '//a[@class="JobListing__container"]'))
#     )
#     urls = [result.get_attribute("href") for result in results]
#     assert any("Kennel Assistant" in result.text for result in results), "No job listings found for 'Kennel Assistant'"

# # Print all URLs
#     for url in urls:
#         print(url)

# try:
#     open_homepage()
#     search_kennel_assistant()
#     then_i_should_see_a_list_of_kennel_assistant_job_urls()
# finally:
#     driver.quit()    



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# @given('I am on the Paycomonline homepage')
# def open_homepage():
#     driver = webdriver.Chrome()
#     driver.get("https://www.paycomonline.net/v4/ats/web.php/jobs?clientkey=FC9962A89833ED19DB7F75E9F964ACB9")

# @when('I enter "Kennel assistant" in the search bar')
# def search_kennel_assistant():
#     search_box = driver.find_element_by_name("quick-search")
#     search_box.send_keys('Kennel assistant')
    

# @then('I should see a list of Kennel Assistant job URLs')
# def then_i_should_see_a_list_of_kennel_assistant_job_urls():
#     global driver
#     time.sleep(5)
#     results = driver.find_elements_by_xpath("//a[contains(@href, 'Kennel+Assistant')]")
#     urls = [result.get_attribute("href") for result in results]
#     assert any("Kennel Assistant" in result.text for result in results), "No job listings found for 'Kennel Assistant'"


# try:
#     open_homepage()
#     search_kennel_assistant()
#     then_i_should_see_a_list_of_kennel_assistant_job_urls()
# finally:
#     driver.quit()             

