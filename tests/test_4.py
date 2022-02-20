from Pages.CartPage import CartPage
from Pages.ProductsPage import ProductsPage


class Test4:

    def test_adicionar_produto_para_compra(self, login_site):
        product_1 = 'Sauce Labs Fleece Jacket'
        products_page = ProductsPage(driver=login_site.driver)
        products_page.add_product_to_cart_by_name(product_1)
        assert products_page.get_cart_number() == '1', "Número do carrinho está incorreto!"
        products_page.open_cart()
        cart_page = CartPage(products_page.driver)
        assert cart_page.is_cart_url(), 'Página do Cart não encontrada!'
        assert cart_page.has_product_item_in_list(product_1), 'Produto não encontrado na lista!'

