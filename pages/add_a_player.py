import time
from pages.base_page import BasePage

class AddAPlayer(BasePage):

    expected_title = 'Add player'
    adding_a_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'

    adding_a_player_hyperlink_xpath = "//div[2]/div/div/a/button/span[1]"

    def getting_the_title(self):
        time.sleep(5)
        assert self.get_page_title(self.adding_a_player_url) == self.expected_title

    def click_on_add_a_player_hyperlink(self):
        self.click_on_the_element(self.adding_a_player_hyperlink_xpath)
