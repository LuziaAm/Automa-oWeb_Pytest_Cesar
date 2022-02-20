from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class CheckoutCompletePage(PageObject):
    url = 'https://www.saucedemo.com/checkout-complete.html'
    class_title = 'title'
    txt_title_page = 'CHECKOUT: COMPLETE!'

    def __init__(self, driver):
        super(CheckoutCompletePage, self).__init__(driver=driver)

    def is_checkout_complete_page(self):
        title_page = self.driver.find_element(By.CLASS_NAME, self.class_title).text
        return self.driver.current_url == self.url and title_page == self.txt_title_page





