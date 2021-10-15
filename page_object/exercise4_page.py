from page_object.common_page import CommonPage


class Exercise4Page(CommonPage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_input_by_its_group_and_value_param(self, group, value_param):
        self.click_by_xpath(f'//h5[text()="{group}"]/../input[@value="{value_param}"]')
