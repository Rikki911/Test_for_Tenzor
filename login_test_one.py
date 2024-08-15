import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from tests_page.login_page_one import MainPage
from tests_page.login_page_one import Aboutpage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(20)
    yield driver
    driver.close()
    driver.quit()

def test_login(driver):
    login_page = MainPage(driver)
    login_page.open_page("https://sbis.ru/")
    login_page.click_contacts()
    login_page.click_tenzor()

    try:
        element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Сила в людях')]")))
        assert element is not None, "Сила не найдена"

        driver.execute_script("arguments[0].scrollIntoView();", element)

        login_page.click_more()
        time.sleep(3)

        expected_url = "https://tensor.ru/about"
        current_url = driver.current_url
        assert current_url == expected_url, "URL is not correct"

        # Переход на страницу About и проверка фотографий
        about_page = AboutPage(driver)
        assert about_page.is_work_section_present(), "Work section is not present"
        about_page.verify_photos_size()

    except TimeoutException:
        pytest.fail("Сила в людях не найдена")
