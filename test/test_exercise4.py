from helpers.url_helper import get_exercise_full_url_by_exercise_number
from page_object.exercise4_page import Exercise4Page


class TestExercise4:
    def test_radio_buttons(self, page):
        page.goto(get_exercise_full_url_by_exercise_number(4))
        exercise_4_page = Exercise4Page(page)

        exercise_4_page.check_checkbox_by_its_group_and_value_param("Group 0:", "v20")
        exercise_4_page.assert_trail_by_value("[2, -1, -1, -1]")
        exercise_4_page.check_checkbox_by_its_group_and_value_param("Group 1:", "v21")
        exercise_4_page.assert_trail_by_value("[2, 2, -1, -1]")
        exercise_4_page.check_checkbox_by_its_group_and_value_param("Group 2:", "v02")
        exercise_4_page.assert_trail_by_value("[2, 2, 0, -1]")
        exercise_4_page.check_checkbox_by_its_group_and_value_param("Group 3:", "v23")
        exercise_4_page.assert_trail_by_value("[2, 2, 0, 2]")

        exercise_4_page.click_check_solution_button()
        exercise_4_page.assert_trail_by_value("OK. Good answer")
