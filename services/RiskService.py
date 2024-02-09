from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def risk_service(data):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://sanctionssearch.ofac.treas.gov/")
        print(data)
        if "name" in data:
            name_input = driver.find_element(By.ID, "ctl00_MainContent_txtLastName")
            name_input.send_keys(data["name"])

        if "address" in data:
            address_input = driver.find_element(By.ID, "ctl00_MainContent_txtAddress")
            address_input.send_keys(data["address"])

        if "city" in data:
            city_input = driver.find_element(By.ID, "ctl00_MainContent_txtCity")
            city_input.send_keys(data["city"])

        if "id" in data:
            id_input = driver.find_element(By.ID, "ctl00_MainContent_txtID")
            id_input.send_keys(data["id"])

        if "type" in data:
            id_input = driver.find_element(By.ID, "ctl00_MainContent_ddlType")
            id_input.send_keys(data["type"])

        search_button = driver.find_element(By.ID, "ctl00_MainContent_btnSearch")
        search_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "gvSearchResults"))
        )

        results = []
        rows = driver.find_elements(By.CSS_SELECTOR, "#gvSearchResults tr:not(:first-child)")
        print(rows)
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            result = {
                "name": cells[0].text,
                "address": cells[1].text,
                "type": cells[2].text,
                "program": cells[3].text,
                "list": cells[4].text,
                "score": cells[5].text
            }
            results.append(result)
        print(results)
        return results
    finally:
        driver.quit()
