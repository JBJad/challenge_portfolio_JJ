from page.base_page import BasePage

class AddAMatchForm(BasePage):
    players_team_field_xpath = "//input[@name='myTeam']"
    opponent_team_field_xpath = "//input[@name='enemyTeam']"
    goals_field_xpath = "//input[@name='myTeamScore']"
    lost_goals_field_xpath = "//input[@name='enemyTeamScore']"
    date_field_xpath = "//input[@name='date']"
    matchAtHome_field_xpath = "//fieldset/div/label[1]/span[1]"
    matchOutside_field_xpath= "//fieldset/div/label[2]/span[1]"
    shirt_colour_field_xpath = "//input[@name='tshirt']"
    league_field_xpath = "//input[@name='league']"
    submit_button_xpath = "//button[@type='submit']"
    clear_button_xpath = "//form/div[3]/button[2]"
    pass
