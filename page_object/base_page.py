from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_by_xpath(self, xpath):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return self.driver.find_element_by_xpath(xpath)

    def click_by_xpath(self, xpath):
        self.find_by_xpath(xpath).click()

    def fill_with_value_by_xpath(self, xpath, value_to_fill):
        self.find_by_xpath(xpath).send_keys(value_to_fill)

    def get_text_of_element_by_xpath(self, xpath):
        return self.find_by_xpath(xpath).text
