from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up options (optional, you can omit if not needed)
chrome_options = Options()

# Path to chromedriver
service = Service(executable_path="/usr/local/bin/chromedriver")

# Create the browser instance
chrome_browser = webdriver.Chrome(service=service, options=chrome_options)

chrome_browser.get("https://www.google.com")

chrome_browser.maximize_window()

'./chromedriver --version'
