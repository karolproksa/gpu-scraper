import time
from selenium.webdriver.common.by import By
#Simple assignment
from selenium.webdriver import Firefox

driver = Firefox()

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def getGTX1080TI():
    ALGTX1080TI = "https://allegrolokalnie.pl/oferty/q/gtx%201080%20ti?typ=kup-teraz&sort=price-asc"
    driver.get(ALGTX1080TI)
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[2]/button[2]").click()

    gpuName = driver.find_elements(By.CLASS_NAME, "offer-card__title")
    gpuPrice = driver.find_elements(By.CLASS_NAME, "price")

    print(color.GREEN + color.BOLD + "========================================================================")
    print("GTX 1080 Ti")
    print("========================================================================" + color.END)
    
    n = 0
    while n<17:
        print(gpuName[n].text + "\n" + color.BOLD + color.CYAN + gpuPrice[n].text + color.END)
        print(color.GREEN + "------------------------------------------------------------------------" + color.END)
        n += 1

getGTX1080TI()
