import time
import sys
sys.path.insert(0, './database')
import connection
from _init_ import getDriver
import testGettingProce as prices
import emailsend



running = True
driver = getDriver()
while running:
    
    sql = "SELECT * From items1"
    cr = connection.getCursor()
    cr.execute(sql)
    alldata = cr.fetchall()

    for data in alldata:
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
            print("rebate")
            try:
                emailsend.sendemail(email, oldPrice, price, name, link)
            except:
                print("error")

    time.sleep(60)
    
    
