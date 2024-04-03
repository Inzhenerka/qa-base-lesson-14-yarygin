from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set the path to where your ChromeDriver is located
chromedriver_path = "/usr/bin/chromedriver"

# Options for Chrome
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')  # Ignores certificate errors
options.add_argument('--headless')  # Runs Chrome in headless mode
options.add_argument('--disable-gpu')  # Disables GPU hardware acceleration; might not be necessary, but can help in some environments
options.add_argument('--no-sandbox')  # Bypass OS security model; often necessary on Linux
options.add_argument('--window-size=1920x1080')  # Sets the initial window size, which can affect responsive web pages
options.add_argument('--ignore-certificate-errors')

# Initialize the driver with Service
s = Service(chromedriver_path)
driver = webdriver.Chrome(service=s, options=options)

# Open the page
driver.get("http://qa-stand-login.inzhenerka.tech/login")

# Example: You can print the page title to verify it loaded correctly
print(driver.title)

# Keep the browser window open for 10 seconds (or any time you prefer)
import time
time.sleep(10)

# Close the browser window
driver.quit()
