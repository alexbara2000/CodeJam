import sys
sys.path.insert(0, '../')
from _init_ import getDriver
import testGettingProce as scrapper


class item:
    def __init__(self, url):
        driver = getDriver('../chromedriver.exe')
        driver.get(url)
        self.url =  url
        self.name = scrapper.getname()
        self.price = scrapper.getPrice()
    
    def printItem(self):
        print(self.url + self.name + self.price)



#x = item("https://www.amazon.ca/TCL-50S425-CA-Ultra-Smart-Television/dp/B07KG318MQ/ref=sr_1_5?dchild=1&keywords=tv&qid=1605318869&sr=8-5")

#print(x.price)

#driver = getDriver('../chromedriver.exe')
driver = getDriver('../chromedriver.exe')
driver.get("https://www.amazon.ca/TCL-50S425-CA-Ultra-Smart-Television/dp/B07KG318MQ/ref=sr_1_5?dchild=1&keywords=tv&qid=1605318869&sr=8-5")

print(scrapper.getname())