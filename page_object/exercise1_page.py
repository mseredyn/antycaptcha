from page_object.common_page import CommonPage


class Exercise1Page(CommonPage):
    B1_BUTTON = "//button[@id='btnButton1']"
    B2_BUTTON = "//button[@id='btnButton2']"

    def __init__(self, driver):
        super().__init__(driver)

    def click_b1_button(self):
        self.click_by_xpath(self.B1_BUTTON)

    def click_b2_button(self):
        self.click_by_xpath(self.B2_BUTTON)
