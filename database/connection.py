import pymysql
db = pymysql.connect(
    host='us-cdbr-east-02.cleardb.com',
    user='bc9047f246620c',
    password='fec4305d',
    db='heroku_bd0b73b73c741f0')


cr = db.cursor()

def getConnection():
    return db

def getCursor():
    return cr

def getRowsFromItem1():
    sql = 'SELECT * FROM items1'
    cr.execute(sql)
    return cr.fetchall()


def UpdatePrice(url, newPrice):
    sql = f'SELECT * FROM items1 WHERE url=\'{url}\''
    cr.execute(sql)
    old = cr.fetchone()
    sql = f'DELETE FROM items1 WHERE url=\'{url}\''
    cr.execute(sql)
    sql = f'Insert INTO items1 (url, name,Price , email) VALUES (\'{old[1]}\', \'{old[2]}\',\'{newPrice}\', \'{old[4]}\')'
    cr.execute(sql)
    db.commit()
