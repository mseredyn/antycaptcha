from page_object.base_page import BasePage


class CommonPage(BasePage):
    CHECK_SOLUTION_BUTTON = "//button[@id='solution']"
    TRAIL = "//code[@class='wrap']"

    def __init__(self, driver):
        super().__init__(driver)

    def click_check_solution_button(self):
        self.click_by_xpath(self.CHECK_SOLUTION_BUTTON)

    def get_trail_value(self):
        return self.get_text_of_element_by_xpath(self.TRAIL)

    def find_trail_by_value(self, value):
        return self.find_by_xpath(f'//code[@class="wrap" and text()="{value}"]')
