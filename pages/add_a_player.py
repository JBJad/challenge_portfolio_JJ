from pages.base_page import BasePage


class AddAPlayer(BasePage):
    players_name_field_xpath = '//div/div[2]/div/div/input'
    players_surname_field_xpath = '//div/div[3]/div/div/input'
    players_age_field_xpath = '//div/div[7]/div/div/input'
    players_main_position_field_xpath = '//div[11]/div/div/input'
    submit_button_xpath = '//form/div[3]/button[1]/span[1]'

    expected_required_text_info = 'Required'
    expected_required_text_info_xpath = '//div/div[11]/div/p'

    def type_in_player_name(self, name):
        self.field_send_keys(self.players_name_field_xpath, name)

    def type_in_player_surname(self, surname):
        self.field_send_keys(self.players_surname_field_xpath, surname)

    def type_in_player_age(self, age):
        self.field_send_keys(self.players_age_field_xpath, age)

    def type_in_player_main_position(self, main_position):
        self.field_send_keys(self.players_main_position_field_xpath, main_position)

    def submit_the_add_a_player_form(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        self.click_on_the_element(self.submit_button_xpath)

    def comparing_text_when_a_required_field_is_empty(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        self.assert_element_text(self.driver, self.expected_required_text_info_xpath, self.expected_required_text_info)

