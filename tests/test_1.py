class Test1:

    def test_click_login_button(self, setup_login_page):
        print('Clicar no botao login')
        setup_login_page.click_login_btn()
        print('Verificar URL login')
        assert setup_login_page.is_url_login(), 'Página não encontrada!'
        print('Verificar mensagem de erro')
        assert setup_login_page.has_login_error_message(), 'Mensagem de erro não encontrada!'


