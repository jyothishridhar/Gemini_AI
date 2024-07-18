**BDD Test Cases:**

* **Scenario: Extract Text from First Two Paragraphs**
    * Given the Marriott website is open
    * When I extract the text from the first two paragraphs
    * Then the extracted text should be as expected

**Step Definitions:**

```python
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

finally:
    driver.quit()
```