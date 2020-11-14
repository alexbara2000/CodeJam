from selenium import webdriver
PATH = "chromedriver.exe"

def getDriver():
     return webdriver.Chrome(PATH)

