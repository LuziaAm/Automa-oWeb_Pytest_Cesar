from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class PageObject:
    def __init__(self, browser=None, driver=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome' or not browser:
                service_chrome = ChromeService(executable_path=ChromeDriverManager().install())
                self.driver = webdriver.Chrome(service=service_chrome)
            elif browser == 'firefox':
                service_firefox = FirefoxService(executable_path=GeckoDriverManager().install())
                self.driver = webdriver.Firefox(service=service_firefox)
            elif browser == 'safari':
                self.driver = webdriver.Safari()
            self.driver.implicitly_wait(2)
            self.driver.maximize_window()

    def close(self):
        self.driver.quit()


