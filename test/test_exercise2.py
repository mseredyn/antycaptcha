from helpers.url_helper import get_exercise_full_url_by_exercise_number
from page_object.exercise2_page import Exercise2Page


class TestExercise2:

    def test_editbox(self, webdriver_factory):
        driver = webdriver_factory.get(get_exercise_full_url_by_exercise_number(2))
        page = Exercise2Page(driver)

        page.clear_t14_input()
        page.fill_t14_input_with_value("Western perhaps.")
        page.click_b1_button()
        page.find_trail_by_value("t14:Western perhaps.b1")

        page.click_check_solution_button()
        page.find_trail_by_value("OK. Good answer")
