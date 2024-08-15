import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class MainPage:

    contacts = (By.XPATH, "//a[text()='Контакты']") #Локатор условно первый Контакты
    tenzor = (By.XPATH, "//a[@class='sbisru-Contacts__logo-tensor mb-12']") #Локатор условно 2 ой Тензор
    people = (By.XPATH, "//p[contains(text(), 'Сила в людях')]") #Проверка Сила в Людях
    more = (By.XPATH, "//a[@href='/about'][contains(text(), 'Подробнее')]")

    def __init__(self, driver):
        self.driver = driver


    def open_page(self, url):
        self.driver.get(url)
        time.sleep(10)


    def click_contacts(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.contacts))
        element.click()

    def click_tenzor(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.tenzor))
        element.click()

    def check_people(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.people)
            )
            return True, "Блок найден"
        except:
            return False, "Блок не найден"


    def verify_people(self):
        try:
            # Ожидаем появления элемента с текстом "Сила в людях"
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.people)
            )
            return True  # Если элемент найден
        except TimeoutException:
            print("Текст 'Сила в людях' не найден за отведенное время.")
            return False


    def click_more(self):
        more = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.more)).more.click()

class AboutPage:
    WORK_SECTION_TITLE = (By.CSS_SELECTOR, 'h2.tensor_ru-header-h2.tensor_ru-About__block-title')
    WORK_SECTION_PHOTOS = (By.CSS_SELECTOR, 'div.s-Grid-container img.tensor_ru-About__block3-image')

    def __init__(self, driver):
        self.driver = driver

    def is_work_section_present(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.WORK_SECTION_TITLE)
        )

    def get_photos(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.WORK_SECTION_PHOTOS)
        )

    def verify_photos_size(self):
        photos = self.get_photos()
        if not photos:
            raise AssertionError("No photos found in the Work section")

        first_photo = photos[0]
        first_photo_width = first_photo.get_attribute('width')
        first_photo_height = first_photo.get_attribute('height')

        for photo in photos:
            width = photo.get_attribute('width')
            height = photo.get_attribute('height')
            assert width == first_photo_width, "Width of photos are not equal"
            assert height == first_photo_height, "Height of photos are not equal"
