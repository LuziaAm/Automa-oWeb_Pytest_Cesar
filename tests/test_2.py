from Pages.ProductsPage import ProductsPage


class Test2:

    def test_efetuar_login(self, setup_login_page):
        setup_login_page.efetuar_login()
        products_page = ProductsPage(setup_login_page.driver)
        assert products_page.is_products_url(), 'Página não encontrada!'
        assert products_page.has_products_title(), 'Título PRODUCTS não encontrado!'
        assert products_page.has_product_list(), 'Lista de produtos não encontrada!'
