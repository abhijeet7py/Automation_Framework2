# Page locators
# Page Actions
# Webdriver -initialization
# custom functions
# No assertion here (They are not test cases)

from seleniumpagefactory.Pagefactory import PageFactory
from tests.utils.common_utils import webdriver_wait
from selenium.webdriver.common.by import By

class LoginPage(PageFactory):
    def __init__(self,driver):
        self.driver = driver
        self.highlight = True

    locators = {
        'username': ('CSS', "#login-username"),
        'password': ('NAME', 'password'),
        'error_message': ('CSS', '#js-notification-box-msg'),
        'submit_button': ('XPATH', '//button[@id="js-login-btn"]')
    }

    def login_to_vwo(self, user, pwd):
        self.username.set_text(user)
        self.password.set_text(pwd)
        self.submit_button.click_button()

    def error_msg(self):
        return self.error_message.get_text()