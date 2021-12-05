import geckodriver_autoinstaller
import time
from selenium.webdriver.common.by import By

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

geckodriver_autoinstaller.install()

# Headless run
options = Options()
options.headless = True

driver = Firefox(options=options)
# driver = Firefox()
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

# Nvidia GPUs
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

# AMD GPUs
def getRX470():
    allegroLokalnieLink = "https://allegrolokalnie.pl/oferty/q/rx%20470?typ=kup-teraz&sort=price-asc"
    driver.get(allegroLokalnieLink)

    gpuName = driver.find_elements(By.CLASS_NAME, "offer-card__title")
    gpuPrice = driver.find_elements(By.CLASS_NAME, "price")

    print(color.RED + color.BOLD +
          "========================================================================")
    print("RX 470")
    print("========================================================================" + color.END)

    n = 0
    for gpus in gpuName:
        print(gpuName[n].text + "\n" + color.BOLD +
              color.YELLOW + gpuPrice[n].text + color.END)
        print(color.RED + "------------------------------------------------------------------------" + color.END)
        n += 1

def getRX480():
    allegroLokalnieLink = "https://allegrolokalnie.pl/oferty/q/rx%20480?typ=kup-teraz&sort=price-asc"
    driver.get(allegroLokalnieLink)

    gpuName = driver.find_elements(By.CLASS_NAME, "offer-card__title")
    gpuPrice = driver.find_elements(By.CLASS_NAME, "price")

    print(color.RED + color.BOLD +
          "========================================================================")
    print("RX 480")
    print("========================================================================" + color.END)

    n = 0
    for gpus in gpuName:
        print(gpuName[n].text + "\n" + color.BOLD +
              color.YELLOW + gpuPrice[n].text + color.END)
        print(color.RED + "------------------------------------------------------------------------" + color.END)
        n += 1

def getRX570():
    allegroLokalnieLink = "https://allegrolokalnie.pl/oferty/q/rx%20570?typ=kup-teraz&sort=price-asc"
    driver.get(allegroLokalnieLink)

    gpuName = driver.find_elements(By.CLASS_NAME, "offer-card__title")
    gpuPrice = driver.find_elements(By.CLASS_NAME, "price")

    print(color.RED + color.BOLD +
          "========================================================================")
    print("RX 570")
    print("========================================================================" + color.END)

    n = 0
    for gpus in gpuName:
        print(gpuName[n].text + "\n" + color.BOLD +
              color.YELLOW + gpuPrice[n].text + color.END)
        print(color.RED + "------------------------------------------------------------------------" + color.END)
        n += 1

def getRX580():
    allegroLokalnieLink = "https://allegrolokalnie.pl/oferty/q/rx%20580?typ=kup-teraz&sort=price-asc"
    driver.get(allegroLokalnieLink)

    gpuName = driver.find_elements(By.CLASS_NAME, "offer-card__title")
    gpuPrice = driver.find_elements(By.CLASS_NAME, "price")

    print(color.RED + color.BOLD +
          "========================================================================")
    print("RX 580")
    print("========================================================================" + color.END)

    n = 0
    for gpus in gpuName:
        print(gpuName[n].text + "\n" + color.BOLD +
              color.YELLOW + gpuPrice[n].text + color.END)
        print(color.RED + "------------------------------------------------------------------------" + color.END)
        n += 1

def getRX5600XT():
    allegroLokalnieLink = "https://allegrolokalnie.pl/oferty/q/rx%205600?typ=kup-teraz&sort=price-asc"
    driver.get(allegroLokalnieLink)

    gpuName = driver.find_elements(By.CLASS_NAME, "offer-card__title")
    gpuPrice = driver.find_elements(By.CLASS_NAME, "price")

    print(color.RED + color.BOLD +
          "========================================================================")
    print("RX 5600 XT")
    print("========================================================================" + color.END)

    n = 0
    for gpus in gpuName:
        print(gpuName[n].text + "\n" + color.BOLD +
              color.YELLOW + gpuPrice[n].text + color.END)
        print(color.RED + "------------------------------------------------------------------------" + color.END)
        n += 1

def getRX5700():
    allegroLokalnieLink = "https://allegrolokalnie.pl/oferty/q/rx%205600?typ=kup-teraz&sort=price-asc"
    driver.get(allegroLokalnieLink)

    gpuName = driver.find_elements(By.CLASS_NAME, "offer-card__title")
    gpuPrice = driver.find_elements(By.CLASS_NAME, "price")

    print(color.RED + color.BOLD +
          "========================================================================")
    print("RX 5700")
    print("========================================================================" + color.END)

    n = 0
    for gpus in gpuName:
        print(gpuName[n].text + "\n" + color.BOLD +
              color.YELLOW + gpuPrice[n].text + color.END)
        print(color.RED + "------------------------------------------------------------------------" + color.END)
        n += 1

def getRX6600XT():
    allegroLokalnieLink = "https://allegrolokalnie.pl/oferty/q/rx%206600?typ=kup-teraz&sort=price-asc"
    driver.get(allegroLokalnieLink)

    gpuName = driver.find_elements(By.CLASS_NAME, "offer-card__title")
    gpuPrice = driver.find_elements(By.CLASS_NAME, "price")

    print(color.RED + color.BOLD +
          "========================================================================")
    print("RX 6600 XT")
    print("========================================================================" + color.END)

    n = 0
    for gpus in gpuName:
        print(gpuName[n].text + "\n" + color.BOLD +
              color.YELLOW + gpuPrice[n].text + color.END)
        print(color.RED + "------------------------------------------------------------------------" + color.END)
        n += 1

def getRX6700():
    allegroLokalnieLink = "https://allegrolokalnie.pl/oferty/q/rx%206700?typ=kup-teraz&sort=price-asc"
    driver.get(allegroLokalnieLink)

    gpuName = driver.find_elements(By.CLASS_NAME, "offer-card__title")
    gpuPrice = driver.find_elements(By.CLASS_NAME, "price")

    print(color.RED + color.BOLD +
          "========================================================================")
    print("RX 6700")
    print("========================================================================" + color.END)

    n = 0
    for gpus in gpuName:
        print(gpuName[n].text + "\n" + color.BOLD +
              color.YELLOW + gpuPrice[n].text + color.END)
        print(color.RED + "------------------------------------------------------------------------" + color.END)
        n += 1

def getRX6800():
    allegroLokalnieLink = "https://allegrolokalnie.pl/oferty/q/rx%206800?typ=kup-teraz&sort=price-asc"
    driver.get(allegroLokalnieLink)

    gpuName = driver.find_elements(By.CLASS_NAME, "offer-card__title")
    gpuPrice = driver.find_elements(By.CLASS_NAME, "price")

    print(color.RED + color.BOLD +
          "========================================================================")
    print("RX 6800")
    print("========================================================================" + color.END)

    n = 0
    for gpus in gpuName:
        print(gpuName[n].text + "\n" + color.BOLD +
              color.YELLOW + gpuPrice[n].text + color.END)
        print(color.RED + "------------------------------------------------------------------------" + color.END)
        n += 1

# Get Nvidia GPUs    
getGTX1080TI()
getRTX2070()
getRTX3060TI()
getRTX3070()
getRTX3080()
getRTX3080TI()
getRTX3090()

# Get AMD GPUs
# Scraping some GPUs might fail because of Allegro's rate limits. If you are looking for a particular model, then you can comment out other ones, to make the script work.
# Usually the script only fails to scrape two or three models. Nothing I can do about it.
getRX470()
getRX480()
getRX570()
getRX580()
getRX5600XT()
getRX5700()
getRX6600XT()
getRX6700()
getRX6800()