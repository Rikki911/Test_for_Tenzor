import pytest
import requests
import os
from re_main_page import MainPage
from re_download_page import DownloadPage

def test_download_plugin(driver):
    main_page = MainPage(driver)
    download_page = DownloadPage(driver)

    main_page.open_page()
    main_page.click_download_link()

    download_url = download_page.download_plugin()
    expected_file_size = download_page.get_expected_file_size()

    # Скачиваем файл
    response = requests.get(download_url, stream=True)
    download_path = os.path.join(os.getcwd(), "sbisplugin-setup-web.exe")

    with open(download_path, 'wb') as file:
        file.write(response.content)

    # Проверка размера файла
    downloaded_file_size = os.path.getsize(download_path) / (1024 * 1024)  # Перевод в МБ
    assert round(downloaded_file_size, 2) == expected_file_size, \
        f"Размер скачанного файла {downloaded_file_size} МБ не соответствует ожидаемому {expected_file_size} МБ"
