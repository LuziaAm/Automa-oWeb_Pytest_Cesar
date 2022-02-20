import time

from Pages.CheckoutCompletePage import CheckoutCompletePage
from Pages.CheckoutInfoPage import CheckoutInfoPage
from Pages.CheckoutOverviewPage import CheckoutOverviewPage


class Test6:

    def test_realizar_compra_com_sucesso(self, one_product_in_cart):
        one_product_in_cart.click_checkout()
        # Página "CHECKOUT: YOUR INFORMATION" deve ser exibida.
        checkout_info_page = CheckoutInfoPage(driver=one_product_in_cart.driver)
        assert checkout_info_page.is_checkout_info_page(), 'Página Checkout Info não encontrada!'
        checkout_info_page.finish_checkout('Joao', 'da Silva', '9999922')

        checkout_overview_page = CheckoutOverviewPage(driver=checkout_info_page.driver)
        assert checkout_overview_page.is_checkout_overview_page(), 'Página de Checkout Overview não encontrada!'

        product_list = ['Sauce Labs Fleece Jacket']
        assert checkout_overview_page.is_all_products_items_in_checkout_overview(product_list)
        checkout_overview_page.click_finish_btn()
        checkout_complete_page = CheckoutCompletePage(driver=checkout_overview_page.driver)
        assert checkout_complete_page.is_checkout_complete_page(), 'Página de Checkout complete page não encontrada!'


