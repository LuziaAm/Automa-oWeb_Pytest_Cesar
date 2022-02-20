import pytest

from Pages.CartPage import CartPage
from Pages.LoginPage import LoginPage
from Pages.ProductsPage import ProductsPage


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help='Browser test')


@pytest.fixture()
def browser(request):
    select_browser = request.config.getoption('browser').lower()
    if select_browser not in ['chrome', 'firefox', 'safari']:
        select_browser = 'chrome'
    return select_browser


@pytest.fixture()
def setup_login_page(browser):
    login_page = LoginPage(browser=browser)
    yield login_page
    login_page.close()


@pytest.fixture()
def login_site_firefox():
    login_page = LoginPage(browser='firefox')
    login_page.efetuar_login()
    yield login_page
    login_page.close()


@pytest.fixture()
def login_site(browser):
    login_page = LoginPage(browser=browser)
    login_page.efetuar_login()
    yield login_page
    login_page.close()


@pytest.fixture()
def one_product_in_cart(browser):
    login_page = LoginPage(browser=browser)
    login_page.efetuar_login()
    product_1 = 'Sauce Labs Fleece Jacket'
    products_page = ProductsPage(driver=login_page.driver)
    products_page.add_product_to_cart_by_name(product_1)
    products_page.open_cart()
    cart_page = CartPage(driver=products_page.driver)
    assert cart_page.has_product_item_in_list(product_1), 'Produto não encontrado na lista!'
    yield cart_page
    login_page.close()