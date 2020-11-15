from _init_ import getDriver
import testGettingProce as prices
import sys
sys.path.insert(0, '.\objects')
sys.path.insert(0, '.\database')
import item



driver = getDriver()
email = input("what is your email?")
link = ""
while link != "n":
    try:
        link = input("If you want to exit, please press n then enter. Please enter an amzaon link to track the price: ")
        if link == "n":
            break
        item.item(link, email,"chromedriver.exe").insertDB()
    except:
        print("404 error")





import server
    





