from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from bs4 import BeautifulSoup
import time
import re

# setting up the browser - running the browser in headless mode
firefox_options = Options()
firefox_options.add_argument("--headless")
driver = webdriver.Firefox(options=firefox_options)
driver.get("https://www.accuweather.com")

try:
    # searching on the website
    search_bar = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
    city_name = input("Enter the City's name: ")
    search_bar.send_keys(city_name)
    time.sleep(5)
    search_bar.send_keys(Keys.ARROW_DOWN)
    search_bar.send_keys(Keys.ENTER)

    # new webpage
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CLASS_NAME, 'weather-icon')))
    html_content = driver.page_source

    # soup for html
    soup = BeautifulSoup(html_content, 'html.parser')

    # regex for extracting the temperatures
    temperature = re.findall(r'">([^a-zA-Z]*?)<', str(soup.findAll('div', class_='temp')))
    temperature_real = re.findall(r'RealFeel®([^a-zA-Z]*?)<', str(soup.findAll('div', class_='real-feel')))

    # printing
    print(f'''Current Temperature in {city_name}: {temperature[0]}, RealFeel: {temperature_real[0].strip()}
Tomorrow's weather: \033[1m{temperature[len(temperature)-2]}\033[0m{temperature[len(temperature)-1]}, RealFeel: {temperature_real[len(temperature_real)-1]}''')

except Exception as e:
    print("Error finding search bar:", e)
    driver.quit()
    exit()
finally:
    driver.quit()
