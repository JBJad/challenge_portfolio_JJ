import time
from pages.base_page import BasePage

class Dashboard(BasePage):

    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'

    adding_a_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    adding_a_player_hyperlink_xpath = "//div[2]/div/div/a/button/span[1]"

    activity_text_xpath = '//div[3]/div/div/h2'

    def getting_the_title(self):
        self.wait_for_element_to_be_visible(self.activity_text_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_add_a_player_hyperlink(self):
        self.click_on_the_element(self.adding_a_player_hyperlink_xpath)


    main_page_hyperlink_xpath = "//ul[1]/div[1]"
    players_page_hyperlink_xpath = "//ul[1]/div[2]"
    language_change_to_English_xpath = "//span[text()='English']"
    language_change_to_Polish_xpath = "//span[text()='Polski']"
    signout_hyperlink_xpath = "//ul[2]/div[2]"
    devteamcontact_hyperlink_xpath = "//*[text() ='Dev team contact']"
    addplayer_hyperlink_xpath = "//div[2]/div/div/a/button"
    playerscount_number_xpath = "//div[2]/div[1]/div/div[2]/b"
    matchescount_number_xpath = "//div[2]/div[2]/div/div[2]/b"
    reportscount_number_xpath = "//div[2]/div[3]/div/div[2]/b"
    eventsscount_number_xpath = "//div[2]/div[4]/div/div[2]/b"
    pass
