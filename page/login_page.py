import time
from page.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage(BasePage):
    expected_title = 'Scouts panel - sign in'
    login_url = 'https://scouts-test.futbolkolektyw.pl/en/login?redirected=true'

    expected_title_text = 'Scouts Panel'
    expected_title_text_xpath = '//div/div[1]/h5'

    expected_text_when_failed_login = 'Identifier or password invalid.'
    expected_text_when_failed_login_xpath = '//div[1]/div[3]/span'

    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def getting_the_title(self):
        time.sleep(5)
        assert self.get_page_title(self.login_url) == self.expected_title

    def comparing_title_text(self):
        self.assert_element_text(self.driver, self.expected_title_text_xpath, self.expected_title_text)

    def comparing_text_when_failed_login(self):
        self.wait_for_element_to_be_clickable(self.sign_in_button_xpath)
        self.assert_element_text(self.driver, self.expected_text_when_failed_login_xpath, self.expected_text_when_failed_login)
