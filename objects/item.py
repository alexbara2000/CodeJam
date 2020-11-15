import sys
sys.path.insert(0, '../')
from _init_ import getDriver
import testGettingProce as scrapper
sys.path.insert(0, '../database')
import connection

class item:
    def __init__(self, url):
        data = scrapper.getData(url, "../chromedriver.exe")
        self.url =  url
        self.name = data[1]
        self.price = data[0]
        
    
    def printItem(self):
        print(self.url + self.name + str(self.price))

    def insertDB(self):
        print(self.url)
        sql = f'Insert INTO items (url, name, email) VALUES (\'{self.url}\', \'{self.name}\', \'none\')'
        cr = connection.getCursor()
        cr.execute(sql)
        db = connection.getConnection()
        db.commit()



