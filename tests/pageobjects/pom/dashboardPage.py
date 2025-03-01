# Dashboard Page class

#Page Locators
#Page Actions

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from tests.utils.common_utils import webdriver_wait

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    usr_logged_in = (By.XPATH,"//span[@data-qa='lufexuloga']")

    def get_user_logged_in(self):
        return self.driver.find_element(*DashboardPage.usr_logged_in)

    def get_user_logged_in_text(self):
        webdriver_wait(driver=self.driver,element_tuple=self.usr_logged_in,timeout=5)
        return self.get_user_logged_in().text