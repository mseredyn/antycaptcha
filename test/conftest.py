import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from config.config_manager import ConfigManager


@pytest.fixture(scope="function")
def webdriver_factory():
    class DriverFactory:
        drivers = []

        @classmethod
        def get(cls, url):
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_argument('disable-infobars')
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            driver.get(url)
            cls.drivers.append(driver)
            return driver

    yield DriverFactory()

    for driver in DriverFactory.drivers:
        driver.close()
