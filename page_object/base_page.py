
import logging

LOGGER = logging.getLogger(__name__)
class BasePage:

    def __init__(self, page):
        self.page = page

    def find_by_xpath(self, xpath):
        LOGGER.info(f'Looking for element by xpath: {xpath}')
        element = self.page.locator(f"xpath={xpath}")
        LOGGER.info(f'Found element: {element}')
        return element

    def click_by_xpath(self, xpath):
        LOGGER.info(f'Clicking element by xpath: {xpath}')
        self.find_by_xpath(xpath).click()

    def fill_with_value_by_xpath(self, xpath, value_to_fill):
        LOGGER.info(f'Filling element of xpath: {xpath} with value: {value_to_fill}')
        self.find_by_xpath(xpath).fill(value_to_fill)

    def get_text_of_element_by_xpath(self, xpath):
        LOGGER.info(f'Fetching text of element by xpath: {xpath}')
        text = self.find_by_xpath(xpath).text_content()
        LOGGER.info(f'Found text: {text}')
        return text
