
from selenium.webdriver.common.by import By
from pages.loginpage import LoginPage
from pages.registerpage import RegisterPage

#@pytest.fixture()
#def driver():
   # driver = webdriver.Chrome()
   # driver.maximize_window()
   # driver.implicitly_wait(4)
  #  yield driver


def test_open_s6(driver):
    loginpage = LoginPage(driver)
    loginpage.open()
    loginpage.click_galaxy_s6()
    registerpage = RegisterPage(driver)
    registerpage.check_title_is('Samsung galaxy s6')

    #driver.get('https://demoblaze.com/')
    #galaxy_s6 = driver.find_element(By.XPATH,value='//a[text()="Samsung galaxy s6"]')
   # galaxy_s6.click()
    #title = driver.find_element(By.CSS_SELECTOR, value='h2')
   # assert title.text == 'Samsung galaxy s6'