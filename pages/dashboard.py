import time
from pages.base_page import BasePage

class Dashboard(BasePage):

    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'

    def getting_the_title(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

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
