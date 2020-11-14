import pymysql
db = pymysql.connect(
    host='us-cdbr-east-02.cleardb.com',
    user='bc9047f246620c',
    password='fec4305d',
    db='heroku_bd0b73b73c741f0')


cr = db.cursor()


def getCursor():
    return cr