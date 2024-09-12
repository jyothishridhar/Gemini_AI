from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = None

def open_homepage():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.paycomonline.net/v4/ats/web.php/jobs?clientkey=FC9962A89833ED19DB7F75E9F964ACB9")

def search_kennel_assistant():
    global driver
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'quick-search'))
    )
    search_box.send_keys('Kennel assistant')
    time.sleep(10)
    
def then_i_should_see_a_list_of_kennel_assistant_job_urls():
    global driver
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//a[@class="JobListing__container"]'))
    )
    urls = [result.get_attribute("href") for result in results]
    assert any("Kennel Assistant" in result.text for result in results), "No job listings found for 'Kennel Assistant'"

    # Print all URLs
    for url in urls:
        print(url)

try:
    open_homepage()
    search_kennel_assistant()
    then_i_should_see_a_list_of_kennel_assistant_job_urls()
finally:
    if driver:
        driver.quit()
