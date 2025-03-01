import allure
import pytest
import time
from selenium import webdriver
from tests.constants.constants import Constants
from tests.pageobjects.pom.loginPage import LoginPage
from tests.pageobjects.pom.dashboardPage import DashboardPage

# Assertions and use page object class

# Webdriver start
# User interaction + assertion
# cloase webdriver


@pytest.fixture()
def setup_teardown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.app_url())
    return driver

@allure.epic("VWO login tests")
@allure.feature("TC0 - Negative test case")
@pytest.mark.negative
def test_vwo_login_negative(setup_teardown):
    login_page = LoginPage(driver=setup_teardown)
    login_page.login_to_vwo(usr="abc@gmail.com",pwd="455")
    time.sleep(2)
    error_msg = login_page.get_error_msg_text()
    assert error_msg == "Your email, password, IP address or location did not match"

@allure.epic("VWO login tests")
@allure.feature("TC1 - Positive test case")
@pytest.mark.positive
def test_vweo_login_positive(setup_teardown):
    login_page = LoginPage(driver=setup_teardown)
    login_page.login_to_vwo(usr="abhijeet123@gmail.com",pwd="Abhijeet@0709")
    time.sleep(5)
    dashboard_page = DashboardPage(driver=setup_teardown)
    assert "a j" in dashboard_page.get_user_logged_in_text()