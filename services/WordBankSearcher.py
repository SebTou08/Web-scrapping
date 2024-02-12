from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def world_bank_search(data):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://projects.worldbank.org/en/projects-operations/procurement/debarred-firms")

        WebDriverWait(driver, 20).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ajax-div"))
        )

        search_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "category"))
        )
        search_box.clear()  # Limpia el campo de búsqueda si es necesario
        search_box.send_keys(data["name"])

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".k-grid-content.k-auto-scrollable"))
        )

        results = []
        rows = driver.find_elements(By.CSS_SELECTOR, ".k-grid-content.k-auto-scrollable table tbody tr")
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if cells:
                result = {
                    "entity": cells[0].text,
                    "jurisdiction": cells[1].text,
                    "linked_to": cells[2].text,
                    "source": cells[3].text,
                    "database": "The world bank"
                }
                results.append(result)

        for result in results:
            print(result)
        return {"results": results, "hits": len(results)}
    except:
        return {"results": [], "hits": 0}

    finally:
        driver.quit()


