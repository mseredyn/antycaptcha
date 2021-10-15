from helpers.url_helper import get_exercise_full_url_by_exercise_number
from page_object.exercise1_page import Exercise1Page


class TestExercise1:
    def test_three_buttons(self, webdriver_factory):
        driver = webdriver_factory.get(get_exercise_full_url_by_exercise_number(1))
        page = Exercise1Page(driver)

        page.click_b2_button()
        page.find_trail_by_value("b2")
        page.click_b1_button()
        page.find_trail_by_value("b2b1")
        page.click_b2_button()
        page.find_trail_by_value("b2b1b2")

        page.click_check_solution_button()
        page.find_trail_by_value("OK. Good answer")
