from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class CheckoutOverviewPage(PageObject):
    url = 'https://www.saucedemo.com/checkout-step-two.html'
    class_title = 'title'
    txt_title_page = 'CHECKOUT: OVERVIEW'
    class_product_item_name = 'inventory_item_name'
    id_finish_btn = 'finish'

    def __init__(self, driver):
        super(CheckoutOverviewPage, self).__init__(driver=driver)

    def is_checkout_overview_page(self):
        title_page = self.driver.find_element(By.CLASS_NAME, self.class_title).text
        return self.driver.current_url == self.url and title_page == self.txt_title_page

    def is_all_products_items_in_checkout_overview(self, required_products):
        checkout_products = self.driver.find_elements(By.CLASS_NAME, self.class_product_item_name)
        product_list = []
        for checkout_item in checkout_products:
            product_list.append(checkout_item.text)
        return set(product_list) == set(required_products)

    def click_finish_btn(self):
        self.driver.find_element(By.ID, self.id_finish_btn).click()




