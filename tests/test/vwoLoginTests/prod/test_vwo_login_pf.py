import time
import pytest
import selenium
from selenium import webdriver

from tests.pageobjects.page_factory.loginPage_pf import LoginPage
from tests.pageobjects.page_factory.dashboardPage_pf import DashboardPage
import allure
from tests.utils.common_utils import webdriver_wait,webdriver_wait_url
from allure_commons.types import AttachmentType
from tests.constants.constants import Constants
import logging

@allure.epic("VWO App")
@allure.feature("Login Test")
class TestVWOLogin:

    @pytest.mark.usefixtures("setup")
    # @pytest.mark.qa
    def test_vwo_login_negative(self, setup):
        try:
            LOGGER = logging.getLogger(__name__)
            driver = setup
            driver.get(Constants.app_url())
            loginPage = LoginPage(driver)
            loginPage.login_to_vwo(user=self.username, pwd="123")
            error_msg_element = loginPage.error_msg()
            LOGGER.info("Negative cases done.")
            assert error_msg_element == "Your email, password, IP address or location did not match"

            if "Dashboard" not in driver.title:
                Constants.take_screenshot(driver, "test_vwo_login_negative_tc0")


        except Exception as e:
            print(e)

    def test_vwo_login_positive(self, setup):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting the Testcase")
        driver = setup
        driver.get(Constants.app_url())
        login_page = LoginPage(driver)
        login_page.login_to_vwo(user=self.username, pwd=self.password)
        dashboard_page = DashboardPage(driver)
        username = dashboard_page.user_logged_in_text()
        assert "Dashboard" in driver.title
        assert "a j" == username
        time.sleep(5)

    # @pytest.mark.usefixtures("setup")
    # @pytest.mark.qa
    # def test_vwo_login_negative_tc3(self, setup):
    #     pass
    #
    # @pytest.mark.usefixtures("setup")
    # @pytest.mark.qa
    # def test_vwo_login_negative_tc4(self, setup):
    #     pass