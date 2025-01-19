import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def website_scraping(website):
    """
    Scrapes raw HTML content from the provided URL.
    """
    print("Launching web browser...")
    chrome_driver_path = "./chromedriver.exe"

    # Configure Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(website)
        print("Waiting for page to load...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        print("Page loaded.")
        return driver.page_source
    finally:
        driver.quit()


def extract_body_content(html_content):
    """
    Extracts the body content from raw HTML.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body 
    return str(body_content) if body_content else ""


def clean_body_content(body_content):
    """
    Cleans the body content by removing non-relevant tags.
    """
    soup = BeautifulSoup(body_content, "html.parser")
    for tag in soup(["script", "style", "noscript", "header", "footer"]):
        tag.decompose()
    return soup.get_text(separator="\n")


def split_dom_content(dom_content, max_length=10000):
    """
    Splits the DOM content into smaller chunks for LLM processing.
    """
    return [dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)]


def combine_chunks(dom_chunks, max_combined_length=25000):
    """
    Combines smaller chunks into fewer larger ones.
    """
    combined_chunks = []
    current_chunk = ""
    for chunk in dom_chunks:
        if len(current_chunk) + len(chunk) <= max_combined_length:
            current_chunk += chunk
        else:
            combined_chunks.append(current_chunk)
            current_chunk = chunk
    if current_chunk:
        combined_chunks.append(current_chunk)
    return combined_chunks
