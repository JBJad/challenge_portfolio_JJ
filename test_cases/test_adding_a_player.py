import os
import time
import unittest

from selenium import webdriver

from page.dashboard import Dashboard
from page.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestClickingOnAddAPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/login?redirected=true')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def testLogIn(self):
        user_login = LoginPage(self.driver)
        user_login.getting_the_title()
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.getting_the_title()
        dashboard_page.click_on_add_a_player_hyperlink()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
