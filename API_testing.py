# **Scenario: Fetching All Job Titles and URLs**

# Given I send a GET request to "/jobs"
# When the response is received
# Then the status code should be 200 OK
# And the response should have the following content:
# | Job Title | URL |
# |---|---|
# | Software Engineer | /jobs/1 |
# | Product Manager | /jobs/2 |

# **Scenario: Fetching the Job Description for a Valid Job ID**

# Given I send a GET request to "/jobs/1"
# When the response is received
# Then the status code should be 200 OK
# And the response should have the following content:
# {
#   "jobDescription": "This is the job description for Software Engineer."
# }

# **Scenario: Fetching the Job Description for an Invalid Job ID**

# Given I send a GET request to "/jobs/3"
# When the response is received
# Then the status code should be 404 Not Found
# And the response should have the following content:
# {
#   "error": "Job not found."


from behave import *
import requests
from requests.exceptions import RequestException
import json

# Global variables
driver = None


@given('I send a GET request to "{endpoint}"')
def get_request(context, endpoint):
    try:
        context.response = requests.get(endpoint)
    except RequestException:
        print(f'Failed to send GET request to {endpoint}')
        assert False


@when('the response is received')
def check_status_code(context):
    try:
        assert context.response.status_code == 200
    except AssertionError:
        print(f'Status code is not 200. Actual status code: {context.response.status_code}')
        assert False


@then('the status code should be {status_code}')
def verify_status_code(context, status_code):
    try:
        assert context.response.status_code == int(status_code)
    except AssertionError:
        print(f'Status code is not {status_code}. Actual status code: {context.response.status_code}')
        assert False


@then('the response should have the following content:')
def check_response_content(context):
    try:
        expected_content = context.table
        actual_content = json.loads(context.response.text)
        assert expected_content == actual_content
    except AssertionError:
        print(f'Response content does not match the expected content. Actual content: {context.response.text}')
        assert False


@given('I send a GET request to "/jobs/{job_id}"')
def get_job_by_id(context, job_id):
    try:
        context.response = requests.get(f'/jobs/{job_id}')
    except RequestException:
        print(f'Failed to send GET request to /jobs/{job_id}')
        assert False