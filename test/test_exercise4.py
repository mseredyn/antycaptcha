from helpers.url_helper import get_exercise_full_url_by_exercise_number
from page_object.exercise4_page import Exercise4Page


class TestExercise4:
    def test_radio_buttons(self, webdriver_factory):
        driver = webdriver_factory.get(get_exercise_full_url_by_exercise_number(4))
        page = Exercise4Page(driver)

        page.click_input_by_its_group_and_value_param("Group 0:", "v20")
        page.find_trail_by_value("[2, -1, -1, -1]")
        page.click_input_by_its_group_and_value_param("Group 1:", "v21")
        page.find_trail_by_value("[2, 2, -1, -1]")
        page.click_input_by_its_group_and_value_param("Group 2:", "v02")
        page.find_trail_by_value("[2, 2, 0, -1]")
        page.click_input_by_its_group_and_value_param("Group 3:", "v23")
        page.find_trail_by_value("[2, 2, 0, 2]")

        page.click_check_solution_button()
        page.find_trail_by_value("OK. Good answer")
