from selenium import webdriver
from shutil import which
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By


service = Service(executable_path='./chromedriver.exe')
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_path = which("chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com")
driver.close()