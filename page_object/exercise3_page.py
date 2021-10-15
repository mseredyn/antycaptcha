from page_object.common_page import CommonPage


class Exercise3Page(CommonPage):
    DROP_DOWN = "//select[@id='s13']"

    def __init__(self, driver):
        super().__init__(driver)

    def click_dropdown(self):
        self.click_by_xpath(self.DROP_DOWN)
        
    def click_option_by_text(self, text):
        self.click_by_xpath(f'//option[text()="{text}"]')
