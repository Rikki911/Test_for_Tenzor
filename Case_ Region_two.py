from selenium.webdriver.common.by import By

class SbisLocators:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://sbis.ru/"
        self.contacts_link = (By.XPATH, "//a[@href='/contacts' and contains(@class, 'sbisru-Header__menu-link') and contains(@class, 'sbisru-Header__menu-link--hover')]") # селектор контакты
        self.region_element = (By.XPATH, '//span[text()="Республика Башкортостан" and contains(@class, "sbis_ru-Region-Chooser__text") and contains(@class, "sbis_ru-link")]')  # селектор региона
        self.partners_list = (By.XPATH, '//a[@class="sbisru-link sbisru-Contacts__text--md" and text()="сертифицированный партнер"]')  # Предположительно селектор для списка партнеров
        self.region_selector = (By.XPATH, '//span[@class="sbis_ru-Region-Chooser__text sbis_ru-link" and text()="Республика Башкортостан"]'
)  # селектор региона РБ
        self.kamchatka_option = (By.XPATH, '//span[@title="Камчатский край" and @class="sbis_ru-link"]/span[text()="41 Камчатский край"]'
)  # селектор  Камчатского края

    def open(self):
        self.driver.get(self.url)

    def go_to_contacts(self):
        self.driver.find_element(*self.contacts_link).click()

    def get_current_region(self):
        return self.driver.find_element(*self.region_element).text

    def get_partners_list(self):
        return self.driver.find_elements(*self.partners_list)

    def change_region(self):
        self.driver.find_element(*self.region_selector).click()
        self.driver.find_element(*self.kamchatka_option).click()

    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title
