from helpers.url_helper import get_exercise_full_url_by_exercise_number
from page_object.exercise2_page import Exercise2Page


class TestExercise2:

    def test_editbox(self, page):
        page.goto(get_exercise_full_url_by_exercise_number(2))
        exercise_2_page = Exercise2Page(page)

        exercise_2_page.fill_t14_input_with_value("Western perhaps.")
        exercise_2_page.click_b1_button()
        exercise_2_page.assert_trail_by_value("t14:Western perhaps.b1")

        exercise_2_page.click_check_solution_button()
        exercise_2_page.assert_trail_by_value("OK. Good answer")
