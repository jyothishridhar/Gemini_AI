**BDD Test Cases:**

**Scenario 1: Search for Kennel Assistant**

* Given I am on the Paycomonline homepage
* When I enter "Kennel assistant" in the search bar
* Then I should see a list of jobs related to Kennel assistant

**Step Definitions:**

```python
from selenium import webdriver

@given('I am on the Paycomonline homepage')
def open_homepage():
    driver = webdriver.Chrome()
    driver.get("https://www.paycomonline.net/v4/ats/web.php/jobs?clientkey=FC9962A89833ED19DB7F75E9F964ACB9")

@when('I enter "Kennel assistant" in the search bar')
def search_kennel_assistant():
    search_box = driver.find_element_by_name('keyword')
    search_box.send_keys('Kennel assistant')
    search_button = driver.find_element_by_id('searchButton')
    search_button.click()

@then('I should see a list of jobs related to Kennel assistant')
def verify_results():
    results = driver.find_elements_by_class_name('jobTitle')
    for result in results:
        assert 'Kennel assistant' in result.text
```

**Try-Finally Block with Step Invocation:**

```python
try:
    open_homepage()
    search_kennel_assistant()
    verify_results()
finally:
    driver.quit()
```