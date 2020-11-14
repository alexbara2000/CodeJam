from selenium import webdriver


def getDriver(PATH = "chromedriver.exe"):
     return webdriver.Chrome(PATH)

