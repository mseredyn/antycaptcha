from hamcrest import assert_that, equal_to

from page_object.base_page import BasePage


class CommonPage(BasePage):
    CHECK_SOLUTION_BUTTON = "//button[@id='solution']"
    TRAIL = "//code[@class='wrap']"

    def __init__(self, page):
        super().__init__(page)

    def click_check_solution_button(self):
        self.click_by_xpath(self.CHECK_SOLUTION_BUTTON)

    def get_trail_value(self):
        return self.get_text_of_element_by_xpath(self.TRAIL)

    def assert_trail_by_value(self, value):
        self.find_by_xpath(f'//code[@class="wrap" and text()="{value}"]').text_content()
