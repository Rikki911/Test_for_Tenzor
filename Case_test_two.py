import time
from selenium import webdriver
from Case2_Region_two import SbisLocators


def test_sbis_region_change():
    driver = webdriver.Chrome()  # Или другой драйвер, если необходимо
    sbis_page = SbisLocators(driver)

    try:
        sbis_page.open()
        sbis_page.go_to_contacts()

        # Проверка региона и списка партнеров
        current_region = sbis_page.get_current_region()
        partners = sbis_page.get_partners_list()

        assert current_region == "Ярославская обл.", f"Ожидался регион 'Ярославская обл.', но был '{current_region}'"
        assert len(partners) > 0, "Список партнеров пуст"

        # Изменение региона на Камчатский край
        sbis_page.change_region()
        time.sleep(2)  # Подождите, пока изменения применятся

        # Проверка нового региона и списка партнеров
        new_region = sbis_page.get_current_region()
        new_partners = sbis_page.get_partners_list()

        assert new_region == "Камчатский край", f"Ожидался регион 'Камчатский край', но был '{new_region}'"
        assert len(new_partners) > 0, "Список партнеров пуст после изменения региона"

        # Проверка URL и title
        expected_url_part = "камчатский"
        expected_title_part = "Камчатский край"

        assert expected_url_part in sbis_page.get_url(), f"URL не содержит '{expected_url_part}'"
        assert expected_title_part in sbis_page.get_title(), f"Title не содержит '{expected_title_part}'"

    finally:
        driver.quit()

if __name__ == "__main__":
    test_sbis_region_change()
