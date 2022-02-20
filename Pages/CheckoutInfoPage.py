from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class CheckoutInfoPage(PageObject):
    url = 'https://www.saucedemo.com/checkout-step-one.html'
    class_title = 'title'
    txt_title_page = 'CHECKOUT: YOUR INFORMATION'
    id_first_name = 'first-name'
    id_last_name = 'last-name'
    id_postal_code = 'postal-code'
    id_continue_btn = 'continue'

    def __init__(self, driver):
        super(CheckoutInfoPage, self).__init__(driver=driver)

    def is_checkout_info_page(self):
        title_page = self.driver.find_element(By.CLASS_NAME, self.class_title).text
        return self.driver.current_url == self.url and title_page == self.txt_title_page

    def finish_checkout(self, first, last_name, zip_code):
        self.driver.find_element(By.ID, self.id_first_name).send_keys(first)
        self.driver.find_element(By.ID, self.id_last_name).send_keys(last_name)
        self.driver.find_element(By.ID, self.id_postal_code).send_keys(zip_code)
        self.driver.find_element(By.ID, self.id_continue_btn).click()

