from selenium.webdriver.common.by import By


class LoginPage:


    def __int__(self,driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://demoblaze.com/')


    def click_galaxy_s6(self):
        galaxy_s6 = self.driver.find_element(By.XPATH, value='//a[text()="Samsung galaxy s6"]')
        galaxy_s6.click()