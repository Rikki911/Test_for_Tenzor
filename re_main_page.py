from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage():
    def __init__(self,driver):
        self.driver = driver
        self.download_link = driver.find_element(By.XPATH, "//a[@href='/download' and contains(@class, 'sbisru-Footer__link')]").click()

    def Open_page(self):
        self.driver.get("https://sbis.ru/")

    def click_download_link(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.download_link)
        )
        element.click()

