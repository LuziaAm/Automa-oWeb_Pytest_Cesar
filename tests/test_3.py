
from Pages.MenuPage import MenuPage


class Test3:

    def test_efetuar_logout(self, login_site_firefox):
        # Abrir menu da aplicação.
        menu_page = MenuPage(login_site_firefox.driver)
        menu_page.open_menu()
        # Menu deve ser exibido.
        assert menu_page.is_menu_open(), "Menu não foi aberto!"
        # Clicar em "LOGOUT".
        menu_page.logout()
        # A aplicação deve retornar para a página inicial de Login.
        assert login_site_firefox.is_url_login(), 'URL de login não encontrada!'

