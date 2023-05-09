import os
import time
import unittest

from selenium import webdriver

from page.add_a_player import AddAPlayer
from page.login_page import LoginPage
from page.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestAddingAPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def testLogIn(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_add_a_player_hyperlink()
        adding_a_player_page = AddAPlayer(self.driver)
        adding_a_player_page.type_in_player_name('Krystian')
        adding_a_player_page.type_in_player_surname('Kowalski')
        adding_a_player_page.type_in_player_age('10-04-1990')
        adding_a_player_page.type_in_player_main_position('offense')
        adding_a_player_page.submit_the_add_a_player_form()
        dashboard_page.getting_the_title()

    @classmethod
    def tearDown(self):
        self.driver.quit()