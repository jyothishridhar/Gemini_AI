**BDD Test Cases**

```
Scenario Outline: Extract Kennel Assistant Job URLs
  Given I am on the Paycomonline homepage
  When I search for "Kennel Assistant"
  Then I extract and print all URLs for "Kennel Assistant"
```

**Step Definitions**

```python
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Adjust the wait time as needed

@given('I am on the Paycomonline homepage')
def step_impl(context):
    try:
        driver.get('https://www.paycomonline.net/v4/ats/web.php/jobs?clientkey=FC9962A89833ED19DB7F75E9F964ACB9')
        print("Passed: Navigated to the homepage")
    except Exception as e:
        print("Failed: Could not navigate to the homepage", e)

@when('I search for "Kennel Assistant"')
def step_impl(context):
    try:
        search_box = driver.find_element(By.ID, 'quick-search')
        search_box.send_keys('Kennel Assistant')
        search_box.submit()
        print("Passed: Searched for Kennel Assistant")
    except Exception as e:
        print("Failed: Could not search for Kennel Assistant", e)

@then('I extract and print all URLs for "Kennel Assistant"')
def step_impl(context):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Kennel Assistant')]")))
        kennel_assistant_links = driver.find_elements(By.XPATH, "//a[contains(text(), 'Kennel Assistant')]")
        for link in kennel_assistant_links:
            print(link.get_attribute('href'))
        print("Passed: Extracted and printed Kennel Assistant URLs")
    except Exception as e:
        print("Failed: Could not extract Kennel Assistant URLs", e)
```

**Usage**

```python
def main():
    try:
        with behave.runner.Context() as context:
            execute_steps(context)
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
```