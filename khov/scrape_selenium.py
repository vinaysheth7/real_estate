# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Initialize Selenium WebDriver (assuming you have ChromeDriver installed)
# # Configure Chrome options
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("executable_path=/Users/abhijitkumar/Documents/updated items - work /Work/home_prices/khov/chromedriver")
#
# # Initialize Selenium WebDriver with Chrome options
# driver = webdriver.Chrome(options=chrome_options)
# # Open the website
# driver.get("https://www.khov.com/find-new-homes/california/indio/92203/k-hovnanian-homes/aguila-at-terra-lago")
#
# # Wait for the button to be clickable (adjust timeout as needed)
# wait = WebDriverWait(driver, 10)
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li[data-link='site-plan-tab']")))
#
# # Click the button
# button.click()
#
# # Wait for the button to be clickable (adjust timeout as needed)
# # wait = WebDriverWait(driver, 10)
# # button = wait.until(EC.element_to_be_clickable((By.ID, "Symbol214")))
# #
# # # Click the button
# # button.click()
#
# # After clicking, you can continue with other actions or scraping
# time.sleep(100)
# print(driver.page_source)
# # Close the browser
# driver.quit()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Selenium WebDriver (assuming you have ChromeDriver installed)
# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("executable_path=/Users/abhijitkumar/Documents/updated items - work /Work/home_prices/khov/chromedriver")

# Initialize Selenium WebDriver with Chrome options
driver = webdriver.Chrome(options=chrome_options)
# Open the website
driver.get("https://khovsecure.ml3ds-cloud.com/?_ga=2.167354750.1161437121.1715801666-156158210.1715801666#/lotmap/162406")

# After clicking, you can continue with other actions or scraping
time.sleep(100)
print(driver.page_source)
# Close the browser
driver.quit()

"interactive-site-plan"
