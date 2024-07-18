import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define driver globally
driver = webdriver.Chrome()
driver.implicitly_wait(10)

@given("the Marriott website is open")
def open_marriott_website():
    try:
        driver.get("https://www.marriott.com/en-us/hotels/dpsav-amarterra-villas-resort-bali-nusa-dua-autograph-collection/overview/")
        print("Website opened successfully")
    except Exception as e:
        print("Failed to open website")

@when("I extract the text from the first two paragraphs")
def extract_paragraph_text():
    try:
        paragraphs = driver.find_elements(By.CSS_SELECTOR, 'p')
        ad_copy1 = " ".join(paragraphs[0].text.split(" ")[:100])
        ad_copy2 = " ".join(paragraphs[1].text.split(" ")[:100])
        print(f"Ad Copy 1: {ad_copy1}\nAd Copy 2: {ad_copy2}")
    except Exception as e:
        print("Failed to extract text")

@then("the extracted text should be as expected")
def verify_extracted_text():
    try:
        expected_ad_copy1 = "Nestled on the secluded shores of Nusa Dua, Amarterra Villas Bali Nusa Dua Autograph Collection offers a captivating fusion of traditional Balinese architecture and modern luxury."
        expected_ad_copy2 = "Immerse yourself in the beauty of our breathtaking beachfront resort, where every detail is designed to create an unforgettable experience."
        assert ad_copy1 == expected_ad_copy1
        assert ad_copy2 == expected_ad_copy2
        print("Extracted text matches the expected values")
    except Exception as e:
        print("Extracted text does not match the expected values")

try:
    open_marriott_website()
    extract_paragraph_text()
    verify_extracted_text()        

finally:
    driver.quit()











# from behave import *
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.implicitly_wait(10)  # Adjust the wait time as needed

# @given('I am on the Paycomonline homepage')
# def step_impl(context):
#     try:
#         driver.get('https://www.paycomonline.net/v4/ats/web.php/jobs?clientkey=FC9962A89833ED19DB7F75E9F964ACB9')
#         print("Passed: Navigated to the homepage")
#     except Exception as e:
#         print("Failed: Could not navigate to the homepage", e)

# @when('I search for "Kennel Assistant"')
# def step_impl(context):
#     try:
#         search_box = driver.find_element(By.ID, 'quick-search')
#         search_box.send_keys('Kennel Assistant')
#         search_box.submit()
#         print("Passed: Searched for Kennel Assistant")
#     except Exception as e:
#         print("Failed: Could not search for Kennel Assistant", e)

# @then('I extract and print all URLs for "Kennel Assistant"')
# def step_impl(context):
#     try:
#         WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Kennel Assistant')]")))
#         kennel_assistant_links = driver.find_elements(By.XPATH, "//a[contains(text(), 'Kennel Assistant')]")
#         for link in kennel_assistant_links:
#             print(link.get_attribute('href'))
#         print("Passed: Extracted and printed Kennel Assistant URLs")
#     except Exception as e:
#         print("Failed: Could not extract Kennel Assistant URLs", e)










