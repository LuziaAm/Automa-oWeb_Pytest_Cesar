from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class CartPage(PageObject):
    url = 'https://www.saucedemo.com/cart.html'
    class_product_item = 'inventory_item_name'
    id_checkout_btn = 'checkout'

    def __init__(self, driver):
        super(CartPage, self).__init__(driver=driver)

    def is_cart_url(self):
        return self.driver.current_url == self.url

    def has_product_item_in_list(self, product_name):
        product_list = self.driver.find_elements(By.CLASS_NAME, self.class_product_item)
        for product_item in product_list:
            if product_item.text == product_name:
                return True
        else:
            return False

    def click_checkout(self):
        self.driver.find_element(By.ID, self.id_checkout_btn).click()

