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


def getData(url):
    driver = getDriver()
    driver.get(url)
    return [getPrice(driver), getname(driver)]





# driver = getDriver()
#links = ["https://www.amazon.ca/TCL-50S425-CA-Ultra-Smart-Television/dp/B07KG318MQ/ref=sr_1_5?dchild=1&keywords=tv&qid=1605318869&sr=8-5","https://www.amazon.ca/dp/B01BPPSBTK/ref=cm_gf_aAN_i1_i3_i6_d_p0_qd0_wPFEEALzidTsfBmMC806","https://www.amazon.ca/dp/B00VTA9F6U/ref=cm_gf_aAN_i14_i19_i3_d_p0_qd0_q73tnhRj2xXY2S5lJSDH"]

#data = getData(links[0])

#print(data)
# for link in links:
#     driver.get(link)
#     price = getPrice()
#     name = getname()

#     print(link)
#     print(name)
#     print(price)

