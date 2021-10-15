from page_object.common_page import CommonPage


class Exercise2Page(CommonPage):
    T14_INPUT_AREA = "//input[@id='t14']"
    B1_BUTTON = "//button[@id='btnButton1']"

    def __init__(self, driver):
        super().__init__(driver)

    def clear_t14_input(self):
        self.find_by_xpath(self.T14_INPUT_AREA).clear()

    def fill_t14_input_with_value(self, value):
        self.fill_with_value_by_xpath(self.T14_INPUT_AREA, value)

    def click_b1_button(self):
        self.click_by_xpath(self.B1_BUTTON)
