
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from googlesearch import search


class ChromeDriverInit:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')  # Run Chrome in headless mode (optional)
        self.chrome_options.add_argument('--no-sandbox')  # Necessary for some server environments
        self.chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
        self.chrome_options.add_argument('--disable-gpu')  # Disable GPU rendering
        self.chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
        self.chrome_service = Service(executable_path="/usr/bin/chromedriver")
        self.driver = webdriver.Chrome(service=self.chrome_service, options=self.chrome_options)


def scrape_google_links(query):
    google_link_list = []
    for j in search(query, tld="co.in", num=5, stop=10, pause=4, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"):
        google_link_list.append(j)
    
    # print(google_link_list)
    return google_link_list


def get_company_names_from_source(url):
    
    driver = ChromeDriverInit().driver
    
    driver.get(url)
    time.sleep(5)  # Allow the page to load fully

    companies = {}

    try:
        # Find company names on the GoodFirms page
        company_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".firm-name a"))
        )
        
        firm_urls = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".firm-urls .visit-website"))
        )

        # Extract company names and their corresponding URLs
        for i, company_tag in enumerate(company_elements):
            company_name = company_tag.text.strip()
            company_url = firm_urls[i].get_attribute('href')
            companies[company_name] = company_url

    except Exception as e:
        print(f"Error while extracting companies: {e}")
    
    driver.quit()
    return companies