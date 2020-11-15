import sys
sys.path.insert(0, '../')
from _init_ import getDriver
import testGettingProce as scrapper
sys.path.insert(0, '../database')
import connection

class item:
    def __init__(self, url, email,ref="../chromedriver.exe"):
        data = scrapper.getData(url, ref)
        self.url =  url
        self.name = data[1]
        self.price = data[0]
        self.email = email
        
    
    def printItem(self):
        print(self.url + self.name + str(self.price))

    def insertDB(self):
        sql = f'Insert INTO items1 (url, name,Price , email) VALUES (\'{self.url}\', \'{self.name}\',\'{self.price}\', \'{self.email}\')'
        cr = connection.getCursor()
        cr.execute(sql)
        db = connection.getConnection()
        db.commit()


