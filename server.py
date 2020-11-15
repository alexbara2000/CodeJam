import time
import sys
sys.path.insert(0, './database')
import connection
from _init_ import getDriver
import testGettingProce as prices
import emailsend
import pymysql


running = True
driver = getDriver()
while running:
    
    db = pymysql.connect(
        host='us-cdbr-east-02.cleardb.com',
        user='bc9047f246620c',
        password='fec4305d',
        db='heroku_bd0b73b73c741f0')
    
    cr = db.cursor()
    alldata = connection.getRowsFromItem1(cr)

    for data in alldata:
        try: 
            link = data[1]
            name = data[2]
            oldPrice = float(data[3])
            email = data[4]
            driver.get(link)
            price = prices.getPrice(driver)
            print(name)
            print(oldPrice)
            print(price)
            print(link)
            if price < oldPrice:
                #in here can you change the price in data base to be the value of "price"
                connection.UpdatePrice(link, price)
                print("rebate")
                try:
                    emailsend.sendemail(email, oldPrice, price, name, link)
                except:
                    print("error")
        except:
            print("error")

    time.sleep(60)
    
    
