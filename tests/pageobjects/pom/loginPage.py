# Login Page class

# Page locators
# Page Actions

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from tests.utils.common_utils import webdriver_wait

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    # Page Locators
    # --> in the form of store the locators/page objects
    username = (By.ID,"login-username")
    password = (By.ID,"login-password")
    submit_button = (By.XPATH,"//button[@id='js-login-btn']")
    error_msg = (By.CSS_SELECTOR,"#js-notification-box-msg")
    # Remove them if you are not using them as of now

    # free_trail = (By.XPATH, "//a[normalize-space()='Start a free trial']")
    # forgot_password_button = (By.XPATH, "//button[normalize-space()='Forgot Password?']")
    # sso_login = (By.XPATH, "//button[normalize-space()='Sign in using SSO']")
    # remember_checkbox = (By.XPATH, "//label[@for='checkbox-remember']//span[@class='checkbox-radio-button ng-scope']//*[name()='svg']")


    # Page Actions
    # write functions to access the page locators

    def get_username(self):
        return self.driver.find_element(*LoginPage.username) #--> Syntax to get the locators

    # (*) means from current class give me the tuple/variable

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_error_message(self):
        webdriver_wait(driver = self.driver,element_tuple = self.error_msg,timeout = 5)
        return self.driver.find_element(*LoginPage.error_msg)

    def login_to_vwo(self,usr,pwd):
        try:
            self.get_username().send_keys(usr)
            self.get_password().send_keys(pwd)
            self.get_submit_button().click()
        except Exception as e:
            print(e)

    def get_error_msg_text(self):
        return self.get_error_message().text
