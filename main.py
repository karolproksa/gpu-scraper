import time
from selenium.webdriver.common.by import By

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

# Headless run
options = Options()
options.headless = True

driver = Firefox(options=options)

# Colors
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
    allegroLokalnieLink = "https://allegrolokalnie.pl/oferty/q/gtx%201080%20ti?typ=kup-teraz&sort=price-asc"
    driver.get(allegroLokalnieLink)
    driver.find_element(
        By.XPATH, "/html/body/div[5]/div/div/div/div[2]/button[2]").click()

    gpuName = driver.find_elements(By.CLASS_NAME, "offer-card__title")
    gpuPrice = driver.find_elements(By.CLASS_NAME, "price")

    print(color.GREEN + color.BOLD +
          "========================================================================")
    print("GTX 1080 Ti")
    print("========================================================================" + color.END)

    n = 0
    for gpus in gpuName:
        print(gpuName[n].text + "\n" + color.BOLD +
              color.CYAN + gpuPrice[n].text + color.END)
        print(color.GREEN + "------------------------------------------------------------------------" + color.END)
        n += 1


def getRTX2070():
    allegroLokalnieLink = "https://allegrolokalnie.pl/oferty/q/rtx%202070?typ=kup-teraz&sort=price-asc"
    driver.get(allegroLokalnieLink)

    gpuName = driver.find_elements(By.CLASS_NAME, "offer-card__title")
    gpuPrice = driver.find_elements(By.CLASS_NAME, "price")

    print(color.GREEN + color.BOLD +
          "========================================================================")
    print("RTX 2070")
    print("========================================================================" + color.END)

    n = 0
    for gpus in gpuName:
        print(gpuName[n].text + "\n" + color.BOLD +
              color.CYAN + gpuPrice[n].text + color.END)
        print(color.GREEN + "------------------------------------------------------------------------" + color.END)
        n += 1


def getRTX3060TI():
    allegroLokalnieLink = "https://allegrolokalnie.pl/oferty/q/rtx%203060%20ti?typ=kup-teraz&sort=price-asc"
    driver.get(allegroLokalnieLink)

    gpuName = driver.find_elements(By.CLASS_NAME, "offer-card__title")
    gpuPrice = driver.find_elements(By.CLASS_NAME, "price")

    print(color.GREEN + color.BOLD +
          "========================================================================")
    print("RTX 3060 Ti")
    print("========================================================================" + color.END)

    n = 0
    for gpus in gpuName:
        print(gpuName[n].text + "\n" + color.BOLD +
              color.CYAN + gpuPrice[n].text + color.END)
        print(color.GREEN + "------------------------------------------------------------------------" + color.END)
        n += 1

def getRTX3070():
    allegroLokalnieLink = "https://allegrolokalnie.pl/oferty/q/rtx%203070?typ=kup-teraz&sort=price-asc"
    driver.get(allegroLokalnieLink)

    gpuName = driver.find_elements(By.CLASS_NAME, "offer-card__title")
    gpuPrice = driver.find_elements(By.CLASS_NAME, "price")

    print(color.GREEN + color.BOLD +
          "========================================================================")
    print("RTX 3070")
    print("========================================================================" + color.END)

    n = 0
    for gpus in gpuName:
        print(gpuName[n].text + "\n" + color.BOLD +
              color.CYAN + gpuPrice[n].text + color.END)
        print(color.GREEN + "------------------------------------------------------------------------" + color.END)
        n += 1

def getRTX3080():
    allegroLokalnieLink = "https://allegrolokalnie.pl/oferty/q/rtx%203080?typ=kup-teraz&sort=price-asc"
    driver.get(allegroLokalnieLink)

    gpuName = driver.find_elements(By.CLASS_NAME, "offer-card__title")
    gpuPrice = driver.find_elements(By.CLASS_NAME, "price")

    print(color.GREEN + color.BOLD +
          "========================================================================")
    print("RTX 3080")
    print("========================================================================" + color.END)

    n = 0
    for gpus in gpuName:
        print(gpuName[n].text + "\n" + color.BOLD +
              color.CYAN + gpuPrice[n].text + color.END)
        print(color.GREEN + "------------------------------------------------------------------------" + color.END)
        n += 1

def getRTX3080TI():
    allegroLokalnieLink = "https://allegrolokalnie.pl/oferty/q/rtx%203080%20ti?typ=kup-teraz&sort=price-asc"
    driver.get(allegroLokalnieLink)

    gpuName = driver.find_elements(By.CLASS_NAME, "offer-card__title")
    gpuPrice = driver.find_elements(By.CLASS_NAME, "price")

    print(color.GREEN + color.BOLD +
          "========================================================================")
    print("RTX 3080 Ti")
    print("========================================================================" + color.END)

    n = 0
    for gpus in gpuName:
        print(gpuName[n].text + "\n" + color.BOLD +
              color.CYAN + gpuPrice[n].text + color.END)
        print(color.GREEN + "------------------------------------------------------------------------" + color.END)
        n += 1

def getRTX3090():
    allegroLokalnieLink = "https://allegrolokalnie.pl/oferty/q/rtx%203090?typ=kup-teraz&sort=price-asc"
    driver.get(allegroLokalnieLink)

    gpuName = driver.find_elements(By.CLASS_NAME, "offer-card__title")
    gpuPrice = driver.find_elements(By.CLASS_NAME, "price")

    print(color.GREEN + color.BOLD +
          "========================================================================")
    print("RTX 3090")
    print("========================================================================" + color.END)

    n = 0
    for gpus in gpuName:
        print(gpuName[n].text + "\n" + color.BOLD +
              color.CYAN + gpuPrice[n].text + color.END)
        print(color.GREEN + "------------------------------------------------------------------------" + color.END)
        n += 1

getGTX1080TI()
getRTX2070()
getRTX3060TI()
getRTX3070()
getRTX3080()
getRTX3080TI()
getRTX3090()
