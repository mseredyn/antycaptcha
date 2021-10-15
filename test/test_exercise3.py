from helpers.url_helper import get_exercise_full_url_by_exercise_number
from page_object.exercise3_page import Exercise3Page


class TestExercise3:
    def test_dropdown_list(self, webdriver_factory):
        driver = webdriver_factory.get(get_exercise_full_url_by_exercise_number(3))
        page = Exercise3Page(driver)

        page.click_dropdown()
        page.click_option_by_text("Verdoro Green")
        page.find_trail_by_value("s13:v2")

        page.click_check_solution_button()
        page.find_trail_by_value("OK. Good answer")
