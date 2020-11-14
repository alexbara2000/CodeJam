from _init_ import getDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = getDriver()
#https://www.amazon.ca/TCL-50S425-CA-Ultra-Smart-Television/dp/B07KG318MQ/ref=sr_1_5?dchild=1&keywords=tv&qid=1605318869&sr=8-5
driver.get("https://www.amazon.ca/iRobot-Roomba-Connected-Automatic-Disposal/dp/B085D45SZF?ref_=Oct_DLandingS_D_93ee8e93_60&smid=A3DWYIK6Y9EEQB")
try:
    priceid = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "price"))
    )

except:
    driver.quit()

price = priceid.text[11:20]
print(price)