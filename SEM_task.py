from behave import given, when, then, step
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define driver globally
driver = webdriver.Chrome()

class Context:
    def __init__(self):
        self.driver = driver

context = Context()

@given('I am on the Marriott website')
def open_marriott_website(context):
    context.driver.get('https://www.marriott.com/en-us/hotels/dpsav-amarterra-villas-resort-bali-nusa-dua-autograph-collection/overview/')

@when('I browse the page and scroll down')
def scroll_down_page(context):
    try:
        # Scroll down the page
        context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    except Exception as e:
        print("Failed to scroll down the page:", e)

@then('I should be able to extract the text of the first two paragraphs that have more than 150 characters')
def extract_paragraph_text(context):
    try:
        # Get all paragraphs
        paragraphs = context.driver.find_elements(By.TAG_NAME, "p")

        # Filter paragraphs with more than 150 characters
        long_paragraphs = [p.text for p in paragraphs if len(p.text) > 150]

        # Print the first two paragraphs
        print("First paragraph:", long_paragraphs[0])
        print("Second paragraph:", long_paragraphs[1])
    except Exception as e:
        print("Failed to extract paragraph text:", e)

@then('I should be able to extract the text of the first two paragraphs that have more than 150 characters in try block')
def extract_paragraph_text_try_block(context):
    try:
        # Get all paragraphs
        paragraphs = context.driver.find_elements(By.TAG_NAME, "p")

        # Filter paragraphs with more than 150 characters
        long_paragraphs = [p.text for p in paragraphs if len(p.text) > 150]

        # Print the first two paragraphs
        print("First paragraph:", long_paragraphs[0])
        print("Second paragraph:", long_paragraphs[1])
    except Exception as e:
        print("Failed to extract paragraph text:", e)
        assert False, "Failed to extract paragraph text"

try:
    open_marriott_website(context)
    scroll_down_page(context)
    extract_paragraph_text(context)
    extract_paragraph_text_try_block(context)
finally:
    driver.quit()
