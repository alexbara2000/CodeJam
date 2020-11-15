from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def getDriver(PATH = "chromedriver.exe"):
     options = Options()
     options.add_argument('--headless')
     options.add_argument('--disable-gpu')  # Last I checked this was necessary.
     return webdriver.Chrome(PATH, chrome_options=options)

