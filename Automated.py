from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import os
import pytest

@pytest.fixture(scope="function")
def setup(request):
    context = {}
    context["browser"] = webdriver.Chrome()
    request.cls.context = context

    def teardown():
        context["browser"].quit()

    request.addfinalizer(teardown)

class TestPaycomonline:

    @allure.tag("Search Job Postings")
    def test_search_job_postings(self, context):
        step_user_is_on_paycomonline_website(context)
        step_user_enters_search_term(context)
        step_search_results_are_displayed(context)

    @allure.tag("Filters")
    def test_filters(self, context):
        step_user_is_on_paycomonline_website(context)
        step_user_clicks_on_filters_button(context)
        step_user_selects_full_time_in_employment_type_filter(context)
        step_only_full_time_job_postings_are_displayed(context)
        step_user_selects_overnight_in_schedule_filter(context)
        step_only_overnight_job_postings_are_displayed(context)

if __name__ == "__main__":
    pytest.main()