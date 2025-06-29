from selenium.webdriver.common.by import By

class RegisterPage:

    def __int__(self,driver):
        self.driver = driver

    def check_title_is(self,title):
        page_title = self.driver.find_element(By.CSS_SELECTOR, value='h2')
        assert page_title.text == title