import os
import time
import unittest

from selenium import webdriver
from page.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class FailedTestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/login?redirected=true')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def testLogIn(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user02@getnadanada.com')
        user_login.type_in_password('Test-1231')
        user_login.click_on_sign_in_button()
        user_login.comparing_text_when_failed_login()

    @classmethod
    def tearDown(self):
        self.driver.quit()
