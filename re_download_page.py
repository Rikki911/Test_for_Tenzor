from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DownloadPage:
    download_plugin_link = (By.XPATH, "//a[@href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe' and contains(@class, 'sbis_ru-DownloadNew-loadLink__link')]")
    expected_file_size_mb = 11.1

    def __init__(self, driver):
        self.driver = driver

    def download_plugin(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.download_plugin_link))
        return element.get_attribute("href")

    def get_expected_file_size(self):
        return self.expected_file_size_mb
