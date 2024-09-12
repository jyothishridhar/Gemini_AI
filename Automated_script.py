```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define the driver globally
driver = webdriver.Chrome()

def open_marriott_website():
    """
    This function opens the Marriott website.
    """
    driver.get("https://www.paycomonline.net/v4/ats/web.php/jobs?clientkey=FC9962A89833ED19DB7F75E9F964ACB9")

def enter_search_term(search_term):
    """
    This function enters the search term in the search bar.

    Args:
        search_term (str): The search term to enter.
    """
    search_bar = driver.find_element(By.ID, "searchbar")
    search_bar.send_keys(search_term)

def click_search_button():
    """
    This function clicks the search button.
    """
    search_button = driver.find_element(By.ID, "searchbutton")
    search_button.click()

def verify_search_results(expected_results):
    """
    This function verifies that the search results page contains a list of jobs that match the search criteria.

    Args:
        expected_results (list): The expected search results.
    """
    results = driver.find_elements(By.CSS_SELECTOR, ".job-listing")
    actual_results = [result.text for result in results]

    assert all(result in actual_results for result in expected_results), "The search results do not match the expected results."

def extract_job_urls(search_term):
    """
    This function extracts the URLs of all the jobs that match the search criteria.

    Args:
        search_term (str): The search term used to filter the results.
    """
    results = driver.find_elements(By.CSS_SELECTOR, ".job-listing")
    job_urls = [result.find_element(By.TAG_NAME, "a").get_attribute("href") for result in results]

    return job_urls

def click_location_filter():
    """
    This function clicks the "Location" filter.
    """
    location_filter = driver.find_element(By.ID, "locationFilter")
    location_filter.click()

def select_location(location):
    """
    This function selects a location from the dropdown menu.

    Args:
        location (str): The location to select.
    """
    location_dropdown = driver.find_element(By.ID, "locationDropdown")
    location_dropdown.select_by_visible_text(location)

def click_apply_button():
    """
    This function clicks the "Apply" button.
    """
    apply_button = driver.find_element(By.ID, "applyButton")
    apply_button.click()

def verify_location_filtered_results(expected_results):
    """
    This function verifies that the results page contains a list of jobs that match the search criteria and are located in the selected location.

    Args:
        expected_results (list): The expected search results.
    """
    results = driver.find_elements(By.CSS_SELECTOR, ".job-listing")
    actual_results = [result.text for result in results]

    assert all(result in actual_results for result in expected_results), "The search results do not match the expected results."

def click_experience_filter():
    """
    This function clicks the "Experience" filter.
    """
    experience_filter = driver.find_element(By.ID, "experienceFilter")
    experience_filter.click()

def select_experience(experience):
    """
    This function selects an experience level from the dropdown menu.

    Args:
        experience (str): The experience level to select.
    """
    experience_dropdown = driver.find_element(By.ID, "experienceDropdown")
    experience_dropdown.select_by_visible_text(experience)

def verify_experience_filtered_results(expected_results):
    """
    This function verifies that the results page contains a list of jobs that match the search criteria and have the selected experience level.

    Args:
        expected_results (list): The expected search results.
    """
    results = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".job-listing")))
    actual_results = [result.text for result in results]

    assert all(result in actual_results for result in expected_results), "The search results do not match the expected results."

try:
    open_marriott_website()
    enter_search_term("Kennel Assistant")
    click_search_button()
    verify_search_results(["Kennel Assistant", "Kennel Technician", "Veterinary Assistant"])
    extract_job_urls("Kennel Assistant")
    click_location_filter()
    select_location("Remote")
    click_apply_button()
    verify_location_filtered_results(["Kennel Assistant", "Veterinary Assistant"])
    extract_job_urls("Kennel Assistant")
    click_experience_filter()
    select_experience("Entry Level")
    click_apply_button()
    verify_experience_filtered_results(["Kennel Assistant", "Veterinary Assistant"])
    extract_job_urls("Kennel Assistant")
finally:
    driver.quit()
```