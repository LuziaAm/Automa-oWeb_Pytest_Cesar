import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class ProductsPage(PageObject):
    url_products = 'https://www.saucedemo.com/inventory.html'
    class_title_page = 'title'
    txt_products_title = 'PRODUCTS'
    class_products_list = 'inventory_list'
    class_product_item = 'inventory_item'
    class_product_name = 'inventory_item_name'
    class_add_to_cart_btn = 'btn_inventory'
    txt_remove_btn = 'REMOVE'
    class_shopping_cart_badge = 'shopping_cart_badge'
    class_shopping_cart_link = 'shopping_cart_link'

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)

    def is_products_url(self):
        return self.driver.current_url == self.url_products

    def has_products_title(self):
        products_title = self.driver.find_element(By.CLASS_NAME, self.class_title_page).text
        return products_title == self.txt_products_title

    def has_product_list(self):
        try:
            self.driver.find_element(By.CLASS_NAME, self.class_products_list)
            return True
        except NoSuchElementException:
            return False

    def add_product_to_cart_by_name(self, product_name):
        product_list = self.driver.find_elements(By.CLASS_NAME, self.class_product_item)

        for product_item in product_list:
            name = product_item.find_element(By.CLASS_NAME, self.class_product_name).text
            if name == product_name:
                product_item.find_element(By.CLASS_NAME, self.class_add_to_cart_btn).click()
                if product_item.find_element(By.CLASS_NAME, self.class_add_to_cart_btn).text != self.txt_remove_btn:
                    raise Exception("Botão não mudou para REMOVE!")
                break
        else:
            raise Exception('Produto não encontrado!!!')

    def get_cart_number(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_shopping_cart_badge).text

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, self.class_shopping_cart_link).click()
