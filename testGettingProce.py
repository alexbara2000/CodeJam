from _init_ import getDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


def getPrice(driver):
    price = 0
    try:
        price = driver.find_element_by_id('priceblock_ourprice').text
        price = convert_price(price)
    except NoSuchElementException:
        try:
            availability = driver.find_element_by_id('availability').text
            if 'Available' in availability:
                price = driver.find_element_by_class_name('olp-padding-right').text
                price = convert_price(price[price.find("$"):])
        except Exception as e:
            return None
    except Exception as e:
        return None
    return price

def convert_price(price):
        price = price.split("$")[1]
        try:
            price = price.split("\n")[0] + "." + price.split("\n")[1]
        except:
            Exception()
        try:
            price = price.split(",")[0] + price.split(",")[1]
        except:
            Exception()
        return float(price)

def getname(driver):
    try:
        return driver.find_element_by_id('productTitle').text
    except Exception as e:
        return None


def getData(url, ref):
    driver = getDriver(ref)
    driver.get(url)
    return [getPrice(driver), getname(driver)]





# driver = getDriver()
# for link in links:
#     driver.get(link)
#     price = getPrice()
#     name = getname()

#     print(link)
#     print(name)
#     print(price)

