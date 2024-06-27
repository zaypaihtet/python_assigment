from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# # Setup Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
# chrome_options.add_argument("--window-size=1920,1080")
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# # Initialize the Chrome driver
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=chrome_options)

# # Open the target webpage
# driver.get("https://mobile.bet365.com/inplaydiaryapi/schedule?timezone=16&lid=33&zid=0")

# # Get the page source
# page_source = driver.page_source

# # Print the page source (or you can parse it using BeautifulSoup if needed)
# print(page_source)

# # Close the driver
# driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Initialize the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


# URL of Bet365 football scores page
url = 'https://www.bet365.com/#/AC/B18/C20604387/D43/E107996749/F43/'

# Open the URL
driver.get(url)

# Wait for the football scores to load
try:
    # Example of waiting for an element that contains the football scores to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.gl-MarketGroup'))
    )

    # Find the elements that contain the football scores
    score_elements = driver.find_elements(By.CSS_SELECTOR, 'div.gl-MarketGroup')

    # Extract and print the scores
    for element in score_elements:
        match_info = element.find_element(By.CSS_SELECTOR, 'div.cm-MarketGroup_Name').text
        scores = element.find_elements(By.CSS_SELECTOR, 'span.soccer-ScoreBoard_Children')
        print(f'Match: {match_info}')
        for score in scores:
            print(f'Score: {score.text}')
        print('---')

finally:
    # Close the WebDriver
    driver.quit()
