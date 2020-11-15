from _init_ import getDriver
import testGettingProce as prices


driver = getDriver()
val = input("what is your email?")
link = ""
while link != "n":
    link = input("If you want to exit, please press n then enter. Please enter an amzaon link to track the price: ")
    driver.get(link)
    price = prices.getPrice(driver)
    name = prices.getname(driver)
    print(name + str(price))





