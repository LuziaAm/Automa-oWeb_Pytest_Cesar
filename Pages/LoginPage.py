from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class LoginPage(PageObject):
    url = 'https://www.saucedemo.com/'
    id_login_button = 'login-button'
    class_error_message = 'error-message-container'
    txt_login_error_message = 'Epic sadface: Username is required'
    id_user_name = 'user-name'
    id_password = 'password'

    def __init__(self, browser=None):
        super(LoginPage, self).__init__(browser=browser)
        self.open_login_page()

    def open_login_page(self):
        self.driver.get(self.url)

    def click_login_btn(self):
        self.driver.find_element(By.ID, self.id_login_button).submit()

    def is_url_login(self):
        return self.driver.current_url == self.url

    def has_login_error_message(self):
        element_error = self.driver.find_element(By.CLASS_NAME, self.class_error_message)
        return element_error.text == self.txt_login_error_message

    def efetuar_login(self, username='standard_user', password='secret_sauce'):
        self.driver.find_element(By.ID, self.id_user_name).send_keys(username)
        self.driver.find_element(By.ID, self.id_password).send_keys(password)
        self.click_login_btn()
