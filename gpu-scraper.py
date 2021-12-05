import geckodriver_autoinstaller
import time
from selenium.webdriver.common.by import By

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from forex_python.converter import CurrencyRates

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


c = CurrencyRates()
Currency = c.get_rate('USD', 'PLN')
# USD price in PLN, for further calculations
usdToPln = round(Currency, 2)

# Nvidia GPUs
def getGTX1060():
    whatToMineLink = "https://whattomine.com/coins?aq_1080Ti=0&aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=0&aq_66xt=0&aq_vii=0&aq_5700xt=0&aq_5700=0&aq_5600xt=0&aq_vega64=0&aq_vega56=0&aq_3090=0&aq_38Ti=0&aq_3080=0&aq_38L=0&aq_37Ti=0&aq_3070=0&aq_37L=0&aq_3060Ti=0&aq_36TiL=0&aq_3060=0&aq_36L=0&aq_55xt8=0&aq_580=0&aq_570=0&aq_480=0&aq_470=0&aq_fury=0&aq_380=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080=0&aq_1070Ti=0&aq_1070=0&aq_10606=1&a_10606=true&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=22.50&factor%5Beth_p%5D=90.00&e4g=true&factor%5Be4g_hr%5D=22.50&factor%5Be4g_p%5D=90.00&zh=true&factor%5Bzh_hr%5D=32.50&factor%5Bzh_p%5D=90.00&cnh=true&factor%5Bcnh_hr%5D=590.00&factor%5Bcnh_p%5D=70.00&cng=true&factor%5Bcng_hr%5D=800.00&factor%5Bcng_p%5D=90.00&cnr=true&factor%5Bcnr_hr%5D=390.00&factor%5Bcnr_p%5D=80.00&cnf=true&factor%5Bcnf_hr%5D=1000.00&factor%5Bcnf_p%5D=70.00&eqa=true&factor%5Beqa_hr%5D=135.00&factor%5Beqa_p%5D=90.00&cc=true&factor%5Bcc_hr%5D=3.40&factor%5Bcc_p%5D=90.00&cr29=true&factor%5Bcr29_hr%5D=3.80&factor%5Bcr29_p%5D=90.00&ct31=true&factor%5Bct31_hr%5D=0.00&factor%5Bct31_p%5D=0.00&ct32=true&factor%5Bct32_hr%5D=0.15&factor%5Bct32_p%5D=90.00&eqb=true&factor%5Beqb_hr%5D=10.70&factor%5Beqb_p%5D=90.00&rmx=true&factor%5Brmx_hr%5D=350.00&factor%5Brmx_p%5D=80.00&ns=true&factor%5Bns_hr%5D=680.00&factor%5Bns_p%5D=90.00&al=true&factor%5Bal_hr%5D=44.50&factor%5Bal_p%5D=90.00&ops=true&factor%5Bops_hr%5D=4.80&factor%5Bops_p%5D=90.00&eqz=true&factor%5Beqz_hr%5D=18.50&factor%5Beqz_p%5D=90.00&zlh=true&factor%5Bzlh_hr%5D=19.50&factor%5Bzlh_p%5D=90.00&kpw=true&factor%5Bkpw_hr%5D=9.00&factor%5Bkpw_p%5D=90.00&ppw=true&factor%5Bppw_hr%5D=9.00&factor%5Bppw_p%5D=90.00&x25x=true&factor%5Bx25x_hr%5D=2.40&factor%5Bx25x_p%5D=90.00&fpw=true&factor%5Bfpw_hr%5D=7.50&factor%5Bfpw_p%5D=90.00&vh=true&factor%5Bvh_hr%5D=0.34&factor%5Bvh_p%5D=80.00&factor%5Bcost%5D=0.15&sort=Profitability24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate"
    driver.get(whatToMineLink)
    getProfitability = driver.find_element(
        By.CSS_SELECTOR, ".table-success > td:nth-child(8) > strong:nth-child(2)")
    profitability = usdToPln * float(getProfitability.text[1:])

    allegroLokalnieLink = "https://allegrolokalnie.pl/oferty/q/gtx%201060?typ=kup-teraz&sort=price-asc"
    driver.get(allegroLokalnieLink)
    driver.find_element(
        By.XPATH, "/html/body/div[5]/div/div/div/div[2]/button[2]").click()

    gpuName = driver.find_elements(By.CLASS_NAME, "offer-card__title")
    gpuPrice = driver.find_elements(By.CLASS_NAME, "price")

    

    print(color.GREEN + color.BOLD +
          "========================================================================")
    print("GTX 1060")
    print("========================================================================" + color.END)

    n = 0
    for gpus in gpuName:
        print(gpuName[n].text + "\n" + color.BOLD +
              color.CYAN + gpuPrice[n].text + color.END)
        roi = float(gpuPrice[n].text[0 : -6]) / profitability
        print("RoI: " + str(round(roi, 2)) + " days")
        print(color.GREEN + "------------------------------------------------------------------------" + color.END)
        n += 1

def getGTX1080TI():
    whatToMineLink = "https://whattomine.com/coins?aq_1080Ti=1&a_1080Ti=true&aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=0&aq_66xt=0&aq_vii=0&aq_5700xt=0&aq_5700=0&aq_5600xt=0&aq_vega64=0&aq_vega56=0&aq_3090=0&aq_38Ti=0&aq_3080=0&aq_38L=0&aq_37Ti=0&aq_3070=0&aq_37L=0&aq_3060Ti=0&aq_36TiL=0&aq_3060=0&aq_36L=0&aq_55xt8=0&aq_580=0&aq_570=0&aq_480=0&aq_470=0&aq_fury=0&aq_380=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080=0&aq_1070Ti=0&aq_1070=0&aq_10606=0&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=39.00&factor%5Beth_p%5D=180.00&e4g=true&factor%5Be4g_hr%5D=49.00&factor%5Be4g_p%5D=180.00&zh=true&factor%5Bzh_hr%5D=86.00&factor%5Bzh_p%5D=200.00&cnh=true&factor%5Bcnh_hr%5D=1060.00&factor%5Bcnh_p%5D=150.00&cng=true&factor%5Bcng_hr%5D=2350.00&factor%5Bcng_p%5D=200.00&cnr=true&factor%5Bcnr_hr%5D=750.00&factor%5Bcnr_p%5D=160.00&cnf=true&factor%5Bcnf_hr%5D=1730.00&factor%5Bcnf_p%5D=150.00&eqa=true&factor%5Beqa_hr%5D=340.00&factor%5Beqa_p%5D=200.00&cc=true&factor%5Bcc_hr%5D=7.90&factor%5Bcc_p%5D=190.00&cr29=true&factor%5Bcr29_hr%5D=8.70&factor%5Bcr29_p%5D=190.00&ct31=true&factor%5Bct31_hr%5D=1.45&factor%5Bct31_p%5D=190.00&ct32=true&factor%5Bct32_hr%5D=0.46&factor%5Bct32_p%5D=190.00&eqb=true&factor%5Beqb_hr%5D=27.30&factor%5Beqb_p%5D=190.00&rmx=true&factor%5Brmx_hr%5D=1030.00&factor%5Brmx_p%5D=160.00&ns=true&factor%5Bns_hr%5D=1900.00&factor%5Bns_p%5D=190.00&al=true&factor%5Bal_hr%5D=87.50&factor%5Bal_p%5D=170.00&ops=true&factor%5Bops_hr%5D=13.60&factor%5Bops_p%5D=200.00&eqz=true&factor%5Beqz_hr%5D=49.00&factor%5Beqz_p%5D=190.00&zlh=true&factor%5Bzlh_hr%5D=50.50&factor%5Bzlh_p%5D=200.00&kpw=true&factor%5Bkpw_hr%5D=21.50&factor%5Bkpw_p%5D=200.00&ppw=true&factor%5Bppw_hr%5D=21.50&factor%5Bppw_p%5D=200.00&x25x=true&factor%5Bx25x_hr%5D=6.90&factor%5Bx25x_p%5D=190.00&fpw=true&factor%5Bfpw_hr%5D=21.50&factor%5Bfpw_p%5D=190.00&vh=true&factor%5Bvh_hr%5D=0.79&factor%5Bvh_p%5D=160.00&factor%5Bcost%5D=0.15&sort=Profitability24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate"
    driver.get(whatToMineLink)
    getProfitability = driver.find_element(
        By.CSS_SELECTOR, ".table-success > td:nth-child(8) > strong:nth-child(2)")
    profitability = usdToPln * float(getProfitability.text[1:])

    allegroLokalnieLink = "https://allegrolokalnie.pl/oferty/q/gtx%201080%20ti?typ=kup-teraz&sort=price-asc"
    driver.get(allegroLokalnieLink)
    
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
        roi = float(gpuPrice[n].text[0 : -6]) / profitability
        print("RoI: " + str(round(roi, 2)) + " days")
        print(color.GREEN + "------------------------------------------------------------------------" + color.END)
        n += 1


def getRTX2070():
    whatToMineLink = "https://whattomine.com/coins?aq_10606=0&aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=0&aq_66xt=0&aq_vii=0&aq_5700xt=0&aq_5700=0&aq_5600xt=0&aq_vega64=0&aq_vega56=0&aq_3090=0&aq_38Ti=0&aq_3080=0&aq_38L=0&aq_37Ti=0&aq_3070=0&aq_37L=0&aq_3060Ti=0&aq_36TiL=0&aq_3060=0&aq_36L=0&aq_55xt8=0&aq_580=0&aq_570=0&aq_480=0&aq_470=0&aq_fury=0&aq_380=0&aq_2080Ti=0&aq_2080=0&aq_2070=1&a_2070=true&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=0&aq_1070Ti=0&aq_1070=0&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=40.00&factor%5Beth_p%5D=140.00&e4g=true&factor%5Be4g_hr%5D=40.00&factor%5Be4g_p%5D=140.00&zh=true&factor%5Bzh_hr%5D=62.00&factor%5Bzh_p%5D=150.00&cnh=true&factor%5Bcnh_hr%5D=970.00&factor%5Bcnh_p%5D=120.00&cng=true&factor%5Bcng_hr%5D=1850.00&factor%5Bcng_p%5D=150.00&cnr=true&factor%5Bcnr_hr%5D=700.00&factor%5Bcnr_p%5D=140.00&cnf=true&factor%5Bcnf_hr%5D=1620.00&factor%5Bcnf_p%5D=120.00&eqa=true&factor%5Beqa_hr%5D=250.00&factor%5Beqa_p%5D=150.00&cc=true&factor%5Bcc_hr%5D=7.70&factor%5Bcc_p%5D=150.00&cr29=true&factor%5Bcr29_hr%5D=7.70&factor%5Bcr29_p%5D=150.00&ct31=true&factor%5Bct31_hr%5D=1.15&factor%5Bct31_p%5D=150.00&ct32=true&factor%5Bct32_hr%5D=0.37&factor%5Bct32_p%5D=150.00&eqb=true&factor%5Beqb_hr%5D=23.00&factor%5Beqb_p%5D=150.00&rmx=true&factor%5Brmx_hr%5D=700.00&factor%5Brmx_p%5D=140.00&ns=true&factor%5Bns_hr%5D=1700.00&factor%5Bns_p%5D=150.00&al=true&factor%5Bal_hr%5D=65.00&factor%5Bal_p%5D=140.00&ops=true&factor%5Bops_hr%5D=37.00&factor%5Bops_p%5D=150.00&eqz=true&factor%5Beqz_hr%5D=34.10&factor%5Beqz_p%5D=150.00&zlh=true&factor%5Bzlh_hr%5D=46.00&factor%5Bzlh_p%5D=150.00&kpw=true&factor%5Bkpw_hr%5D=21.00&factor%5Bkpw_p%5D=150.00&ppw=true&factor%5Bppw_hr%5D=21.00&factor%5Bppw_p%5D=150.00&x25x=true&factor%5Bx25x_hr%5D=4.80&factor%5Bx25x_p%5D=150.00&fpw=true&factor%5Bfpw_hr%5D=20.00&factor%5Bfpw_p%5D=140.00&vh=true&factor%5Bvh_hr%5D=0.59&factor%5Bvh_p%5D=130.00&factor%5Bcost%5D=0.15&sort=Profitability24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate"
    driver.get(whatToMineLink)
    getProfitability = driver.find_element(
        By.CSS_SELECTOR, ".table-success > td:nth-child(8) > strong:nth-child(2)")
    profitability = usdToPln * float(getProfitability.text[1:])

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
        roi = float(gpuPrice[n].text[0 : -6]) / profitability
        print("RoI: " + str(round(roi, 2)) + " days")
        print(color.GREEN + "------------------------------------------------------------------------" + color.END)
        n += 1


def getRTX3060TI():
    whatToMineLink = "https://whattomine.com/coins?aq_2070=1&aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=0&aq_66xt=0&aq_vii=0&aq_5700xt=0&aq_5700=0&aq_5600xt=0&aq_vega64=0&aq_vega56=0&aq_3090=0&aq_38Ti=0&aq_3080=0&aq_38L=0&aq_37Ti=0&aq_3070=0&aq_37L=0&aq_3060Ti=1&a_3060Ti=true&aq_36TiL=0&aq_3060=0&aq_36L=0&aq_55xt8=0&aq_580=0&aq_570=0&aq_480=0&aq_470=0&aq_fury=0&aq_380=0&aq_2080Ti=0&aq_2080=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=0&aq_1070Ti=0&aq_1070=0&aq_10606=0&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=58.10&factor%5Beth_p%5D=130.00&e4g=true&factor%5Be4g_hr%5D=58.10&factor%5Be4g_p%5D=130.00&zh=true&factor%5Bzh_hr%5D=0.00&factor%5Bzh_p%5D=0.00&cnh=true&factor%5Bcnh_hr%5D=0.00&factor%5Bcnh_p%5D=0.00&cng=true&factor%5Bcng_hr%5D=2850.00&factor%5Bcng_p%5D=190.00&cnr=true&factor%5Bcnr_hr%5D=0.00&factor%5Bcnr_p%5D=0.00&cnf=true&factor%5Bcnf_hr%5D=0.00&factor%5Bcnf_p%5D=0.00&eqa=true&factor%5Beqa_hr%5D=370.00&factor%5Beqa_p%5D=190.00&cc=true&factor%5Bcc_hr%5D=9.80&factor%5Bcc_p%5D=190.00&cr29=true&factor%5Bcr29_hr%5D=9.70&factor%5Bcr29_p%5D=190.00&ct31=true&factor%5Bct31_hr%5D=0.55&factor%5Bct31_p%5D=190.00&ct32=true&factor%5Bct32_hr%5D=0.50&factor%5Bct32_p%5D=190.00&eqb=true&factor%5Beqb_hr%5D=32.50&factor%5Beqb_p%5D=190.00&rmx=true&factor%5Brmx_hr%5D=0.00&factor%5Brmx_p%5D=0.00&ns=true&factor%5Bns_hr%5D=0.00&factor%5Bns_p%5D=0.00&al=true&factor%5Bal_hr%5D=160.00&factor%5Bal_p%5D=130.00&ops=true&factor%5Bops_hr%5D=48.00&factor%5Bops_p%5D=190.00&eqz=true&factor%5Beqz_hr%5D=0.00&factor%5Beqz_p%5D=0.00&zlh=true&factor%5Bzlh_hr%5D=54.50&factor%5Bzlh_p%5D=190.00&kpw=true&factor%5Bkpw_hr%5D=27.00&factor%5Bkpw_p%5D=190.00&ppw=true&factor%5Bppw_hr%5D=26.00&factor%5Bppw_p%5D=190.00&x25x=true&factor%5Bx25x_hr%5D=0.00&factor%5Bx25x_p%5D=0.00&fpw=true&factor%5Bfpw_hr%5D=25.00&factor%5Bfpw_p%5D=150.00&vh=true&factor%5Bvh_hr%5D=1.19&factor%5Bvh_p%5D=140.00&factor%5Bcost%5D=0.15&sort=Profitability24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate"
    driver.get(whatToMineLink)
    getProfitability = driver.find_element(
        By.CSS_SELECTOR, ".table-success > td:nth-child(8) > strong:nth-child(2)")
    profitability = usdToPln * float(getProfitability.text[1:])

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
        roi = float(gpuPrice[n].text[0 : -6]) / profitability
        print("RoI: " + str(round(roi, 2)) + " days")
        print(color.GREEN + "------------------------------------------------------------------------" + color.END)
        n += 1


def getRTX3070():
    whatToMineLink = "https://whattomine.com/coins?aq_3070=1&a_3070=true&aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=0&aq_66xt=0&aq_vii=0&aq_5700xt=0&aq_5700=0&aq_5600xt=0&aq_vega64=0&aq_vega56=0&aq_3090=0&aq_38Ti=0&aq_3080=0&aq_38L=0&aq_37Ti=0&aq_37L=0&aq_3060Ti=0&aq_36TiL=0&aq_3060=0&aq_36L=0&aq_55xt8=0&aq_580=0&aq_570=0&aq_480=0&aq_470=0&aq_fury=0&aq_380=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=0&aq_1070Ti=0&aq_1070=0&aq_10606=0&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=58.1&factor%5Beth_p%5D=130.0&e4g=true&factor%5Be4g_hr%5D=58.1&factor%5Be4g_p%5D=130.0&zh=true&factor%5Bzh_hr%5D=100.0&factor%5Bzh_p%5D=180.0&cnh=true&factor%5Bcnh_hr%5D=1750.0&factor%5Bcnh_p%5D=180.0&cng=true&factor%5Bcng_hr%5D=2900.0&factor%5Bcng_p%5D=180.0&cnr=true&factor%5Bcnr_hr%5D=0.0&factor%5Bcnr_p%5D=0.0&cnf=true&factor%5Bcnf_hr%5D=3400.0&factor%5Bcnf_p%5D=170.0&eqa=true&factor%5Beqa_hr%5D=390.0&factor%5Beqa_p%5D=180.0&cc=true&factor%5Bcc_hr%5D=10.2&factor%5Bcc_p%5D=180.0&cr29=true&factor%5Bcr29_hr%5D=10.3&factor%5Bcr29_p%5D=180.0&ct31=true&factor%5Bct31_hr%5D=0.0&factor%5Bct31_p%5D=0.0&ct32=true&factor%5Bct32_hr%5D=0.5&factor%5Bct32_p%5D=180.0&eqb=true&factor%5Beqb_hr%5D=34.0&factor%5Beqb_p%5D=180.0&rmx=true&factor%5Brmx_hr%5D=1030.0&factor%5Brmx_p%5D=160.0&ns=true&factor%5Bns_hr%5D=0.0&factor%5Bns_p%5D=0.0&al=true&factor%5Bal_hr%5D=160.0&factor%5Bal_p%5D=130.0&ops=true&factor%5Bops_hr%5D=52.7&factor%5Bops_p%5D=180.0&eqz=true&factor%5Beqz_hr%5D=55.0&factor%5Beqz_p%5D=180.0&zlh=true&factor%5Bzlh_hr%5D=61.0&factor%5Bzlh_p%5D=180.0&kpw=true&factor%5Bkpw_hr%5D=27.6&factor%5Bkpw_p%5D=180.0&ppw=true&factor%5Bppw_hr%5D=27.4&factor%5Bppw_p%5D=180.0&x25x=true&factor%5Bx25x_hr%5D=8.0&factor%5Bx25x_p%5D=180.0&fpw=true&factor%5Bfpw_hr%5D=25.0&factor%5Bfpw_p%5D=150.0&vh=true&factor%5Bvh_hr%5D=1.19&factor%5Bvh_p%5D=140.0&factor%5Bcost%5D=0.15&sort=Profitability24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate"
    driver.get(whatToMineLink)
    getProfitability = driver.find_element(
        By.CSS_SELECTOR, ".table-success > td:nth-child(8) > strong:nth-child(2)")
    profitability = usdToPln * float(getProfitability.text[1:])

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
        roi = float(gpuPrice[n].text[0 : -6]) / profitability
        print("RoI: " + str(round(roi, 2)) + " days")
        print(color.GREEN + "------------------------------------------------------------------------" + color.END)
        n += 1


def getRTX3080():
    whatToMineLink = "https://whattomine.com/coins?aq_3070=1&aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=0&aq_66xt=0&aq_vii=0&aq_5700xt=0&aq_5700=0&aq_5600xt=0&aq_vega64=0&aq_vega56=0&aq_3090=0&aq_38Ti=0&aq_3080=1&a_3080=true&aq_38L=0&aq_37Ti=0&aq_37L=0&aq_3060Ti=0&aq_36TiL=0&aq_3060=0&aq_36L=0&aq_55xt8=0&aq_580=0&aq_570=0&aq_480=0&aq_470=0&aq_fury=0&aq_380=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=0&aq_1070Ti=0&aq_1070=0&aq_10606=0&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=91.50&factor%5Beth_p%5D=230.00&e4g=true&factor%5Be4g_hr%5D=91.50&factor%5Be4g_p%5D=230.00&zh=true&factor%5Bzh_hr%5D=134.00&factor%5Bzh_p%5D=250.00&cnh=true&factor%5Bcnh_hr%5D=2400.00&factor%5Bcnh_p%5D=250.00&cng=true&factor%5Bcng_hr%5D=3700.00&factor%5Bcng_p%5D=250.00&cnr=true&factor%5Bcnr_hr%5D=0.00&factor%5Bcnr_p%5D=0.00&cnf=true&factor%5Bcnf_hr%5D=4100.00&factor%5Bcnf_p%5D=250.00&eqa=true&factor%5Beqa_hr%5D=470.00&factor%5Beqa_p%5D=250.00&cc=true&factor%5Bcc_hr%5D=14.20&factor%5Bcc_p%5D=250.00&cr29=true&factor%5Bcr29_hr%5D=14.30&factor%5Bcr29_p%5D=250.00&ct31=true&factor%5Bct31_hr%5D=2.30&factor%5Bct31_p%5D=250.00&ct32=true&factor%5Bct32_hr%5D=0.80&factor%5Bct32_p%5D=250.00&eqb=true&factor%5Beqb_hr%5D=46.50&factor%5Beqb_p%5D=250.00&rmx=true&factor%5Brmx_hr%5D=1500.00&factor%5Brmx_p%5D=250.00&ns=true&factor%5Bns_hr%5D=0.00&factor%5Bns_p%5D=0.00&al=true&factor%5Bal_hr%5D=190.00&factor%5Bal_p%5D=180.00&ops=true&factor%5Bops_hr%5D=77.00&factor%5Bops_p%5D=250.00&eqz=true&factor%5Beqz_hr%5D=63.00&factor%5Beqz_p%5D=250.00&zlh=true&factor%5Bzlh_hr%5D=79.00&factor%5Bzlh_p%5D=250.00&kpw=true&factor%5Bkpw_hr%5D=39.50&factor%5Bkpw_p%5D=250.00&ppw=true&factor%5Bppw_hr%5D=38.90&factor%5Bppw_p%5D=250.00&x25x=true&factor%5Bx25x_hr%5D=11.10&factor%5Bx25x_p%5D=250.00&fpw=true&factor%5Bfpw_hr%5D=41.00&factor%5Bfpw_p%5D=250.00&vh=true&factor%5Bvh_hr%5D=1.45&factor%5Bvh_p%5D=240.00&factor%5Bcost%5D=0.15&sort=Profitability24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate"
    driver.get(whatToMineLink)
    getProfitability = driver.find_element(
        By.CSS_SELECTOR, ".table-success > td:nth-child(8) > strong:nth-child(2)")
    profitability = usdToPln * float(getProfitability.text[1:])

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
        roi = float(gpuPrice[n].text[0 : -6]) / profitability
        print("RoI: " + str(round(roi, 2)) + " days")
        print(color.GREEN + "------------------------------------------------------------------------" + color.END)
        n += 1


def getRTX3080TI():
    whatToMineLink = "https://whattomine.com/coins?aq_38Ti=1&a_38Ti=true&aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=0&aq_66xt=0&aq_vii=0&aq_5700xt=0&aq_5700=0&aq_5600xt=0&aq_vega64=0&aq_vega56=0&aq_3090=0&aq_3080=1&aq_38L=0&aq_37Ti=0&aq_3070=1&aq_37L=0&aq_3060Ti=0&aq_36TiL=0&aq_3060=0&aq_36L=0&aq_55xt8=0&aq_580=0&aq_570=0&aq_480=0&aq_470=0&aq_fury=0&aq_380=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=0&aq_1070Ti=0&aq_1070=0&aq_10606=0&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=85.0&factor%5Beth_p%5D=290.0&e4g=true&factor%5Be4g_hr%5D=85.0&factor%5Be4g_p%5D=290.0&zh=true&factor%5Bzh_hr%5D=0.0&factor%5Bzh_p%5D=0.0&cnh=true&factor%5Bcnh_hr%5D=0.0&factor%5Bcnh_p%5D=0.0&cng=true&factor%5Bcng_hr%5D=4200.0&factor%5Bcng_p%5D=280.0&cnr=true&factor%5Bcnr_hr%5D=0.0&factor%5Bcnr_p%5D=0.0&cnf=true&factor%5Bcnf_hr%5D=0.0&factor%5Bcnf_p%5D=0.0&eqa=true&factor%5Beqa_hr%5D=0.0&factor%5Beqa_p%5D=0.0&cc=true&factor%5Bcc_hr%5D=10.4&factor%5Bcc_p%5D=280.0&cr29=true&factor%5Bcr29_hr%5D=0.0&factor%5Bcr29_p%5D=0.0&ct31=true&factor%5Bct31_hr%5D=0.0&factor%5Bct31_p%5D=0.0&ct32=true&factor%5Bct32_hr%5D=0.0&factor%5Bct32_p%5D=0.0&eqb=true&factor%5Beqb_hr%5D=54.0&factor%5Beqb_p%5D=280.0&rmx=true&factor%5Brmx_hr%5D=0.0&factor%5Brmx_p%5D=0.0&ns=true&factor%5Bns_hr%5D=0.0&factor%5Bns_p%5D=0.0&al=true&factor%5Bal_hr%5D=265.0&factor%5Bal_p%5D=280.0&ops=true&factor%5Bops_hr%5D=85.0&factor%5Bops_p%5D=280.0&eqz=true&factor%5Beqz_hr%5D=0.0&factor%5Beqz_p%5D=0.0&zlh=true&factor%5Bzlh_hr%5D=79.0&factor%5Bzlh_p%5D=280.0&kpw=true&factor%5Bkpw_hr%5D=49.0&factor%5Bkpw_p%5D=280.0&ppw=true&factor%5Bppw_hr%5D=40.0&factor%5Bppw_p%5D=280.0&x25x=true&factor%5Bx25x_hr%5D=0.0&factor%5Bx25x_p%5D=0.0&fpw=true&factor%5Bfpw_hr%5D=0.0&factor%5Bfpw_p%5D=0.0&vh=true&factor%5Bvh_hr%5D=0.0&factor%5Bvh_p%5D=0.0&factor%5Bcost%5D=0.15&sort=Profitability24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate"
    driver.get(whatToMineLink)
    getProfitability = driver.find_element(
        By.CSS_SELECTOR, ".table-success > td:nth-child(8) > strong:nth-child(2)")
    profitability = usdToPln * float(getProfitability.text[1:])

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
        roi = float(gpuPrice[n].text[0 : -6]) / profitability
        print("RoI: " + str(round(roi, 2)) + " days")
        print(color.GREEN + "------------------------------------------------------------------------" + color.END)
        n += 1


def getRTX3090():
    whatToMineLink = "https://whattomine.com/coins?aq_38Ti=1&aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=0&aq_66xt=0&aq_vii=0&aq_5700xt=0&aq_5700=0&aq_5600xt=0&aq_vega64=0&aq_vega56=0&aq_3090=1&a_3090=true&aq_3080=1&aq_38L=0&aq_37Ti=0&aq_3070=1&aq_37L=0&aq_3060Ti=0&aq_36TiL=0&aq_3060=0&aq_36L=0&aq_55xt8=0&aq_580=0&aq_570=0&aq_480=0&aq_470=0&aq_fury=0&aq_380=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=0&aq_1070Ti=0&aq_1070=0&aq_10606=0&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=114.00&factor%5Beth_p%5D=320.00&e4g=true&factor%5Be4g_hr%5D=114.00&factor%5Be4g_p%5D=320.00&zh=true&factor%5Bzh_hr%5D=155.00&factor%5Bzh_p%5D=290.00&cnh=true&factor%5Bcnh_hr%5D=2650.00&factor%5Bcnh_p%5D=260.00&cng=true&factor%5Bcng_hr%5D=4600.00&factor%5Bcng_p%5D=260.00&cnr=true&factor%5Bcnr_hr%5D=0.00&factor%5Bcnr_p%5D=0.00&cnf=true&factor%5Bcnf_hr%5D=5100.00&factor%5Bcnf_p%5D=260.00&eqa=true&factor%5Beqa_hr%5D=510.00&factor%5Beqa_p%5D=290.00&cc=true&factor%5Bcc_hr%5D=13.90&factor%5Bcc_p%5D=290.00&cr29=true&factor%5Bcr29_hr%5D=13.90&factor%5Bcr29_p%5D=290.00&ct31=true&factor%5Bct31_hr%5D=2.70&factor%5Bct31_p%5D=290.00&ct32=true&factor%5Bct32_hr%5D=1.00&factor%5Bct32_p%5D=290.00&eqb=true&factor%5Beqb_hr%5D=52.00&factor%5Beqb_p%5D=290.00&rmx=true&factor%5Brmx_hr%5D=2000.00&factor%5Brmx_p%5D=290.00&ns=true&factor%5Bns_hr%5D=0.00&factor%5Bns_p%5D=0.00&al=true&factor%5Bal_hr%5D=238.00&factor%5Bal_p%5D=240.00&ops=true&factor%5Bops_hr%5D=94.00&factor%5Bops_p%5D=330.00&eqz=true&factor%5Beqz_hr%5D=93.00&factor%5Beqz_p%5D=290.00&zlh=true&factor%5Bzlh_hr%5D=90.00&factor%5Bzlh_p%5D=290.00&kpw=true&factor%5Bkpw_hr%5D=46.50&factor%5Bkpw_p%5D=330.00&ppw=true&factor%5Bppw_hr%5D=46.00&factor%5Bppw_p%5D=330.00&x25x=true&factor%5Bx25x_hr%5D=12.40&factor%5Bx25x_p%5D=290.00&fpw=true&factor%5Bfpw_hr%5D=43.00&factor%5Bfpw_p%5D=310.00&vh=true&factor%5Bvh_hr%5D=1.85&factor%5Bvh_p%5D=250.00&factor%5Bcost%5D=0.15&sort=Profitability24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate"
    driver.get(whatToMineLink)
    getProfitability = driver.find_element(
        By.CSS_SELECTOR, ".table-success > td:nth-child(8) > strong:nth-child(2)")
    profitability = usdToPln * float(getProfitability.text[1:])

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
        roi = float(gpuPrice[n].text[0 : -6]) / profitability
        print("RoI: " + str(round(roi, 2)) + " days")
        print(color.GREEN + "------------------------------------------------------------------------" + color.END)
        n += 1

# AMD GPUs


def getRX470():
    whatToMineLink = "https://whattomine.com/coins?aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=0&aq_66xt=0&aq_vii=0&aq_5700xt=0&aq_5700=0&aq_5600xt=0&aq_vega64=0&aq_vega56=0&aq_3090=1&aq_38Ti=1&aq_3080=1&aq_38L=0&aq_37Ti=0&aq_3070=1&aq_37L=0&aq_3060Ti=0&aq_36TiL=0&aq_3060=0&aq_36L=0&aq_55xt8=0&aq_580=0&aq_570=0&aq_480=0&aq_470=1&aq_fury=0&aq_380=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=0&aq_1070Ti=0&aq_1070=0&aq_10606=0&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=1.5&factor%5Beth_p%5D=120.0&e4g=true&factor%5Be4g_hr%5D=26.0&factor%5Be4g_p%5D=120.0&zh=true&factor%5Bzh_hr%5D=18.0&factor%5Bzh_p%5D=110.0&cnh=true&factor%5Bcnh_hr%5D=590.0&factor%5Bcnh_p%5D=100.0&cng=true&factor%5Bcng_hr%5D=600.0&factor%5Bcng_p%5D=110.0&cnr=true&factor%5Bcnr_hr%5D=660.0&factor%5Bcnr_p%5D=120.0&cnf=true&factor%5Bcnf_hr%5D=1150.0&factor%5Bcnf_p%5D=100.0&eqa=true&factor%5Beqa_hr%5D=80.0&factor%5Beqa_p%5D=110.0&cc=true&factor%5Bcc_hr%5D=0.0&factor%5Bcc_p%5D=0.0&cr29=true&factor%5Bcr29_hr%5D=0.0&factor%5Bcr29_p%5D=0.0&ct31=true&factor%5Bct31_hr%5D=0.3&factor%5Bct31_p%5D=120.0&ct32=true&factor%5Bct32_hr%5D=0.1&factor%5Bct32_p%5D=120.0&eqb=true&factor%5Beqb_hr%5D=13.5&factor%5Beqb_p%5D=120.0&rmx=true&factor%5Brmx_hr%5D=340.0&factor%5Brmx_p%5D=80.0&ns=true&factor%5Bns_hr%5D=680.0&factor%5Bns_p%5D=140.0&al=true&factor%5Bal_hr%5D=51.5&factor%5Bal_p%5D=110.0&ops=true&factor%5Bops_hr%5D=0.0&factor%5Bops_p%5D=0.0&eqz=true&factor%5Beqz_hr%5D=12.4&factor%5Beqz_p%5D=120.0&zlh=true&factor%5Bzlh_hr%5D=12.0&factor%5Bzlh_p%5D=110.0&kpw=true&factor%5Bkpw_hr%5D=12.5&factor%5Bkpw_p%5D=90.0&ppw=true&factor%5Bppw_hr%5D=7.8&factor%5Bppw_p%5D=130.0&x25x=true&factor%5Bx25x_hr%5D=0.65&factor%5Bx25x_p%5D=75.0&fpw=true&factor%5Bfpw_hr%5D=0.0&factor%5Bfpw_p%5D=0.0&vh=true&factor%5Bvh_hr%5D=0.39&factor%5Bvh_p%5D=100.0&factor%5Bcost%5D=0.15&sort=Profitability24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate"
    driver.get(whatToMineLink)
    getProfitability = driver.find_element(
        By.CSS_SELECTOR, ".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(8) > strong:nth-child(2)")
    profitability = usdToPln * float(getProfitability.text[1:])

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
        roi = float(gpuPrice[n].text[0 : -6]) / profitability
        print("RoI: " + str(round(roi, 2)) + " days")
        print(color.RED + "------------------------------------------------------------------------" + color.END)
        n += 1


def getRX480():
    whatToMineLink = "https://whattomine.com/coins?aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=0&aq_66xt=0&aq_vii=0&aq_5700xt=0&aq_5700=0&aq_5600xt=0&aq_vega64=0&aq_vega56=0&aq_3090=1&aq_38Ti=1&aq_3080=1&aq_38L=0&aq_37Ti=0&aq_3070=1&aq_37L=0&aq_3060Ti=0&aq_36TiL=0&aq_3060=0&aq_36L=0&aq_55xt8=0&aq_580=0&aq_570=0&aq_480=1&a_480=true&aq_470=1&aq_fury=0&aq_380=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=0&aq_1070Ti=0&aq_1070=0&aq_10606=0&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=30.00&factor%5Beth_p%5D=140.00&e4g=true&factor%5Be4g_hr%5D=30.00&factor%5Be4g_p%5D=140.00&zh=true&factor%5Bzh_hr%5D=21.00&factor%5Bzh_p%5D=120.00&cnh=true&factor%5Bcnh_hr%5D=960.00&factor%5Bcnh_p%5D=110.00&cng=true&factor%5Bcng_hr%5D=760.00&factor%5Bcng_p%5D=120.00&cnr=true&factor%5Bcnr_hr%5D=830.00&factor%5Bcnr_p%5D=130.00&cnf=true&factor%5Bcnf_hr%5D=1650.00&factor%5Bcnf_p%5D=110.00&eqa=true&factor%5Beqa_hr%5D=95.00&factor%5Beqa_p%5D=120.00&cc=true&factor%5Bcc_hr%5D=2.60&factor%5Bcc_p%5D=130.00&cr29=true&factor%5Bcr29_hr%5D=2.40&factor%5Bcr29_p%5D=130.00&ct31=true&factor%5Bct31_hr%5D=0.60&factor%5Bct31_p%5D=120.00&ct32=true&factor%5Bct32_hr%5D=0.16&factor%5Bct32_p%5D=120.00&eqb=true&factor%5Beqb_hr%5D=15.50&factor%5Beqb_p%5D=140.00&rmx=true&factor%5Brmx_hr%5D=470.00&factor%5Brmx_p%5D=90.00&ns=true&factor%5Bns_hr%5D=820.00&factor%5Bns_p%5D=150.00&al=true&factor%5Bal_hr%5D=59.00&factor%5Bal_p%5D=130.00&ops=true&factor%5Bops_hr%5D=4.90&factor%5Bops_p%5D=120.00&eqz=true&factor%5Beqz_hr%5D=14.00&factor%5Beqz_p%5D=130.00&zlh=true&factor%5Bzlh_hr%5D=14.00&factor%5Bzlh_p%5D=120.00&kpw=true&factor%5Bkpw_hr%5D=13.00&factor%5Bkpw_p%5D=170.00&ppw=true&factor%5Bppw_hr%5D=9.40&factor%5Bppw_p%5D=140.00&x25x=true&factor%5Bx25x_hr%5D=0.83&factor%5Bx25x_p%5D=80.00&fpw=true&factor%5Bfpw_hr%5D=14.50&factor%5Bfpw_p%5D=170.00&vh=true&factor%5Bvh_hr%5D=0.44&factor%5Bvh_p%5D=120.00&factor%5Bcost%5D=0.15&sort=Profitability24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate"
    driver.get(whatToMineLink)
    getProfitability = driver.find_element(
        By.CSS_SELECTOR, ".table-success > td:nth-child(8) > strong:nth-child(2)")
    profitability = usdToPln * float(getProfitability.text[1:])

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
        roi = float(gpuPrice[n].text[0 : -6]) / profitability
        print("RoI: " + str(round(roi, 2)) + " days")
        print(color.RED + "------------------------------------------------------------------------" + color.END)
        n += 1


def getRX570():
    whatToMineLink = "https://whattomine.com/coins?aq_480=1&aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=0&aq_66xt=0&aq_vii=0&aq_5700xt=0&aq_5700=0&aq_5600xt=0&aq_vega64=0&aq_vega56=0&aq_3090=1&aq_38Ti=1&aq_3080=1&aq_38L=0&aq_37Ti=0&aq_3070=1&aq_37L=0&aq_3060Ti=0&aq_36TiL=0&aq_3060=0&aq_36L=0&aq_55xt8=0&aq_580=0&aq_570=1&aq_470=1&aq_fury=0&aq_380=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=0&aq_1070Ti=0&aq_1070=0&aq_10606=0&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=1.50&factor%5Beth_p%5D=120.00&e4g=true&factor%5Be4g_hr%5D=27.90&factor%5Be4g_p%5D=120.00&zh=true&factor%5Bzh_hr%5D=19.00&factor%5Bzh_p%5D=100.00&cnh=true&factor%5Bcnh_hr%5D=640.00&factor%5Bcnh_p%5D=110.00&cng=true&factor%5Bcng_hr%5D=640.00&factor%5Bcng_p%5D=110.00&cnr=true&factor%5Bcnr_hr%5D=730.00&factor%5Bcnr_p%5D=120.00&cnf=true&factor%5Bcnf_hr%5D=1250.00&factor%5Bcnf_p%5D=110.00&eqa=true&factor%5Beqa_hr%5D=85.00&factor%5Beqa_p%5D=100.00&cc=true&factor%5Bcc_hr%5D=0.00&factor%5Bcc_p%5D=0.00&cr29=true&factor%5Bcr29_hr%5D=0.00&factor%5Bcr29_p%5D=0.00&ct31=true&factor%5Bct31_hr%5D=0.35&factor%5Bct31_p%5D=110.00&ct32=true&factor%5Bct32_hr%5D=0.10&factor%5Bct32_p%5D=110.00&eqb=true&factor%5Beqb_hr%5D=14.50&factor%5Beqb_p%5D=120.00&rmx=true&factor%5Brmx_hr%5D=390.00&factor%5Brmx_p%5D=80.00&ns=true&factor%5Bns_hr%5D=700.00&factor%5Bns_p%5D=140.00&al=true&factor%5Bal_hr%5D=55.50&factor%5Bal_p%5D=110.00&ops=true&factor%5Bops_hr%5D=0.00&factor%5Bops_p%5D=0.00&eqz=true&factor%5Beqz_hr%5D=12.80&factor%5Beqz_p%5D=110.00&zlh=true&factor%5Bzlh_hr%5D=12.50&factor%5Bzlh_p%5D=100.00&kpw=true&factor%5Bkpw_hr%5D=13.00&factor%5Bkpw_p%5D=80&ppw=true&factor%5Bppw_hr%5D=7.80&factor%5Bppw_p%5D=130.00&x25x=true&factor%5Bx25x_hr%5D=0.70&factor%5Bx25x_p%5D=75.00&fpw=true&factor%5Bfpw_hr%5D=0.00&factor%5Bfpw_p%5D=0.00&vh=true&factor%5Bvh_hr%5D=0.42&factor%5Bvh_p%5D=110.00&factor%5Bcost%5D=0.15&sort=Profitability24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate"
    driver.get(whatToMineLink)
    getProfitability = driver.find_element(
        By.CSS_SELECTOR, ".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(8) > strong:nth-child(2)")
    profitability = usdToPln * float(getProfitability.text[1:])

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
        roi = float(gpuPrice[n].text[0 : -6]) / profitability
        print("RoI: " + str(round(roi, 2)) + " days")
        print(color.RED + "------------------------------------------------------------------------" + color.END)
        n += 1


def getRX580():
    whatToMineLink = "https://whattomine.com/coins?aq_580=1&a_580=true&aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=0&aq_66xt=0&aq_vii=0&aq_5700xt=0&aq_5700=0&aq_5600xt=0&aq_vega64=0&aq_vega56=0&aq_3090=1&aq_38Ti=1&aq_3080=1&aq_38L=0&aq_37Ti=0&aq_3070=1&aq_37L=0&aq_3060Ti=0&aq_36TiL=0&aq_3060=0&aq_36L=0&aq_55xt8=0&aq_570=1&aq_480=1&aq_470=1&aq_fury=0&aq_380=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=0&aq_1070Ti=0&aq_1070=0&aq_10606=0&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=30.5&factor%5Beth_p%5D=130.0&e4g=true&factor%5Be4g_hr%5D=30.5&factor%5Be4g_p%5D=130.0&zh=true&factor%5Bzh_hr%5D=21.0&factor%5Bzh_p%5D=110.0&cnh=true&factor%5Bcnh_hr%5D=960.0&factor%5Bcnh_p%5D=115.0&cng=true&factor%5Bcng_hr%5D=760.0&factor%5Bcng_p%5D=120.0&cnr=true&factor%5Bcnr_hr%5D=830.0&factor%5Bcnr_p%5D=130.0&cnf=true&factor%5Bcnf_hr%5D=1650.0&factor%5Bcnf_p%5D=115.0&eqa=true&factor%5Beqa_hr%5D=95.0&factor%5Beqa_p%5D=110.0&cc=true&factor%5Bcc_hr%5D=2.6&factor%5Bcc_p%5D=120.0&cr29=true&factor%5Bcr29_hr%5D=2.4&factor%5Bcr29_p%5D=120.0&ct31=true&factor%5Bct31_hr%5D=0.6&factor%5Bct31_p%5D=110.0&ct32=true&factor%5Bct32_hr%5D=0.16&factor%5Bct32_p%5D=110.0&eqb=true&factor%5Beqb_hr%5D=15.5&factor%5Beqb_p%5D=130.0&rmx=true&factor%5Brmx_hr%5D=470.0&factor%5Brmx_p%5D=90.0&ns=true&factor%5Bns_hr%5D=820.0&factor%5Bns_p%5D=150.0&al=true&factor%5Bal_hr%5D=59.5&factor%5Bal_p%5D=120.0&ops=true&factor%5Bops_hr%5D=4.9&factor%5Bops_p%5D=110.0&eqz=true&factor%5Beqz_hr%5D=14.0&factor%5Beqz_p%5D=120.0&zlh=true&factor%5Bzlh_hr%5D=14.0&factor%5Bzlh_p%5D=110.0&kpw=true&factor%5Bkpw_hr%5D=13.0&factor%5Bkpw_p%5D=170.0&ppw=true&factor%5Bppw_hr%5D=9.4&factor%5Bppw_p%5D=140.0&x25x=true&factor%5Bx25x_hr%5D=0.83&factor%5Bx25x_p%5D=80.0&fpw=true&factor%5Bfpw_hr%5D=14.5&factor%5Bfpw_p%5D=170.0&vh=true&factor%5Bvh_hr%5D=0.44&factor%5Bvh_p%5D=110.0&factor%5Bcost%5D=0.15&sort=Profitability24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate"
    driver.get(whatToMineLink)
    getProfitability = driver.find_element(
        By.CSS_SELECTOR, ".table-success > td:nth-child(8) > strong:nth-child(2)")
    profitability = usdToPln * float(getProfitability.text[1:])

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
        roi = float(gpuPrice[n].text[0 : -6]) / profitability
        print("RoI: " + str(round(roi, 2)) + " days")
        print(color.RED + "------------------------------------------------------------------------" + color.END)
        n += 1


def getRX5600XT():
    whatToMineLink = "https://whattomine.com/coins?aq_580=0&aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=0&aq_66xt=0&aq_vii=0&aq_5700xt=0&aq_5700=0&aq_5600xt=1&a_5600xt=true&aq_vega64=0&aq_vega56=0&aq_3090=1&aq_38Ti=1&aq_3080=1&aq_38L=0&aq_37Ti=0&aq_3070=1&aq_37L=0&aq_3060Ti=0&aq_36TiL=0&aq_3060=0&aq_36L=0&aq_55xt8=0&aq_570=1&aq_480=1&aq_470=1&aq_fury=0&aq_380=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=0&aq_1070Ti=0&aq_1070=0&aq_10606=0&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=40.50&factor%5Beth_p%5D=110.00&e4g=true&factor%5Be4g_hr%5D=40.50&factor%5Be4g_p%5D=110.00&zh=true&factor%5Bzh_hr%5D=38.00&factor%5Bzh_p%5D=110.00&cnh=true&factor%5Bcnh_hr%5D=0.00&factor%5Bcnh_p%5D=0.00&cng=true&factor%5Bcng_hr%5D=1250.00&factor%5Bcng_p%5D=110.00&cnr=true&factor%5Bcnr_hr%5D=0.00&factor%5Bcnr_p%5D=0.00&cnf=true&factor%5Bcnf_hr%5D=0.00&factor%5Bcnf_p%5D=0.00&eqa=true&factor%5Beqa_hr%5D=0.00&factor%5Beqa_p%5D=0.00&cc=true&factor%5Bcc_hr%5D=3.20&factor%5Bcc_p%5D=80.00&cr29=true&factor%5Bcr29_hr%5D=3.10&factor%5Bcr29_p%5D=80.00&ct31=true&factor%5Bct31_hr%5D=0.50&factor%5Bct31_p%5D=110.00&ct32=true&factor%5Bct32_hr%5D=0.17&factor%5Bct32_p%5D=110.00&eqb=true&factor%5Beqb_hr%5D=20.50&factor%5Beqb_p%5D=110.00&rmx=true&factor%5Brmx_hr%5D=0.00&factor%5Brmx_p%5D=0.00&ns=true&factor%5Bns_hr%5D=0.00&factor%5Bns_p%5D=0.00&al=true&factor%5Bal_hr%5D=80.00&factor%5Bal_p%5D=100.00&ops=true&factor%5Bops_hr%5D=11.50&factor%5Bops_p%5D=90.00&eqz=true&factor%5Beqz_hr%5D=24.20&factor%5Beqz_p%5D=110.00&zlh=true&factor%5Bzlh_hr%5D=23.70&factor%5Bzlh_p%5D=110.00&kpw=true&factor%5Bkpw_hr%5D=17.50&factor%5Bkpw_p%5D=130.00&ppw=true&factor%5Bppw_hr%5D=0.00&factor%5Bppw_p%5D=0.00&x25x=true&factor%5Bx25x_hr%5D=0.00&factor%5Bx25x_p%5D=0.00&fpw=true&factor%5Bfpw_hr%5D=18.00&factor%5Bfpw_p%5D=130.00&vh=true&factor%5Bvh_hr%5D=0.54&factor%5Bvh_p%5D=110.00&factor%5Bcost%5D=0.15&sort=Profitability24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate"
    driver.get(whatToMineLink)
    getProfitability = driver.find_element(
        By.CSS_SELECTOR, ".table-success > td:nth-child(8) > strong:nth-child(2)")
    profitability = usdToPln * float(getProfitability.text[1:])

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
        roi = float(gpuPrice[n].text[0 : -6]) / profitability
        print("RoI: " + str(round(roi, 2)) + " days")
        print(color.RED + "------------------------------------------------------------------------" + color.END)
        n += 1


def getRX5700():
    whatToMineLink = "https://whattomine.com/coins?aq_5600xt=1&aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=0&aq_66xt=0&aq_vii=0&aq_5700xt=1&aq_5700=1&a_5700=true&aq_vega64=0&aq_vega56=0&aq_3090=1&aq_38Ti=1&aq_3080=1&aq_38L=0&aq_37Ti=0&aq_3070=1&aq_37L=0&aq_3060Ti=0&aq_36TiL=0&aq_3060=0&aq_36L=0&aq_55xt8=0&aq_580=0&aq_570=1&aq_480=1&aq_470=1&aq_fury=0&aq_380=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=0&aq_1070Ti=0&aq_1070=0&aq_10606=0&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=55.00&factor%5Beth_p%5D=130.00&e4g=true&factor%5Be4g_hr%5D=55.00&factor%5Be4g_p%5D=130.00&zh=true&factor%5Bzh_hr%5D=46.00&factor%5Bzh_p%5D=140.00&cnh=true&factor%5Bcnh_hr%5D=1350.00&factor%5Bcnh_p%5D=110.00&cng=true&factor%5Bcng_hr%5D=1500.00&factor%5Bcng_p%5D=140.00&cnr=true&factor%5Bcnr_hr%5D=1050.00&factor%5Bcnr_p%5D=110.00&cnf=true&factor%5Bcnf_hr%5D=2000.00&factor%5Bcnf_p%5D=110.00&eqa=true&factor%5Beqa_hr%5D=0.00&factor%5Beqa_p%5D=0.00&cc=true&factor%5Bcc_hr%5D=3.80&factor%5Bcc_p%5D=90.00&cr29=true&factor%5Bcr29_hr%5D=3.70&factor%5Bcr29_p%5D=90.00&ct31=true&factor%5Bct31_hr%5D=1.05&factor%5Bct31_p%5D=130.00&ct32=true&factor%5Bct32_hr%5D=0.35&factor%5Bct32_p%5D=130.00&eqb=true&factor%5Beqb_hr%5D=24.00&factor%5Beqb_p%5D=140.00&rmx=true&factor%5Brmx_hr%5D=0.00&factor%5Brmx_p%5D=0.00&ns=true&factor%5Bns_hr%5D=0.00&factor%5Bns_p%5D=0.00&al=true&factor%5Bal_hr%5D=100.00&factor%5Bal_p%5D=130.00&ops=true&factor%5Bops_hr%5D=13.60&factor%5Bops_p%5D=110.00&eqz=true&factor%5Beqz_hr%5D=30.00&factor%5Beqz_p%5D=140.00&zlh=true&factor%5Bzlh_hr%5D=28.50&factor%5Bzlh_p%5D=140.00&kpw=true&factor%5Bkpw_hr%5D=19.50&factor%5Bkpw_p%5D=160.00&ppw=true&factor%5Bppw_hr%5D=12.00&factor%5Bppw_p%5D=150.00&x25x=true&factor%5Bx25x_hr%5D=0.00&factor%5Bx25x_p%5D=0.00&fpw=true&factor%5Bfpw_hr%5D=21.50&factor%5Bfpw_p%5D=160.00&vh=true&factor%5Bvh_hr%5D=0.71&factor%5Bvh_p%5D=130.00&factor%5Bcost%5D=0.15&sort=Profitability24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate"
    driver.get(whatToMineLink)
    getProfitability = driver.find_element(
        By.CSS_SELECTOR, ".table-success > td:nth-child(8) > strong:nth-child(2)")
    profitability = usdToPln * float(getProfitability.text[1:])

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
        roi = float(gpuPrice[n].text[0 : -6]) / profitability
        print("RoI: " + str(round(roi, 2)) + " days")
        print(color.RED + "------------------------------------------------------------------------" + color.END)
        n += 1


def getRX6600XT():
    whatToMineLink = "https://whattomine.com/coins?aq_5700=1&aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=0&aq_66xt=1&a_66xt=true&aq_vii=0&aq_5700xt=1&aq_5600xt=1&aq_vega64=0&aq_vega56=0&aq_3090=1&aq_38Ti=1&aq_3080=1&aq_38L=0&aq_37Ti=0&aq_3070=1&aq_37L=0&aq_3060Ti=0&aq_36TiL=0&aq_3060=0&aq_36L=0&aq_55xt8=0&aq_580=0&aq_570=1&aq_480=1&aq_470=1&aq_fury=0&aq_380=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=0&aq_1070Ti=0&aq_1070=0&aq_10606=0&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=32.50&factor%5Beth_p%5D=80.00&e4g=true&factor%5Be4g_hr%5D=32.50&factor%5Be4g_p%5D=80.00&zh=true&factor%5Bzh_hr%5D=0.00&factor%5Bzh_p%5D=0.00&cnh=true&factor%5Bcnh_hr%5D=0.00&factor%5Bcnh_p%5D=0.00&cng=true&factor%5Bcng_hr%5D=1350.00&factor%5Bcng_p%5D=80.00&cnr=true&factor%5Bcnr_hr%5D=0.00&factor%5Bcnr_p%5D=0.00&cnf=true&factor%5Bcnf_hr%5D=0.00&factor%5Bcnf_p%5D=0.00&eqa=true&factor%5Beqa_hr%5D=0.00&factor%5Beqa_p%5D=0.00&cc=true&factor%5Bcc_hr%5D=0.00&factor%5Bcc_p%5D=0.00&cr29=true&factor%5Bcr29_hr%5D=0.00&factor%5Bcr29_p%5D=0.00&ct31=true&factor%5Bct31_hr%5D=0.00&factor%5Bct31_p%5D=0.00&ct32=true&factor%5Bct32_hr%5D=0.00&factor%5Bct32_p%5D=0.00&eqb=true&factor%5Beqb_hr%5D=0.00&factor%5Beqb_p%5D=0.00&rmx=true&factor%5Brmx_hr%5D=0.00&factor%5Brmx_p%5D=0.00&ns=true&factor%5Bns_hr%5D=0.00&factor%5Bns_p%5D=0.00&al=true&factor%5Bal_hr%5D=62.00&factor%5Bal_p%5D=80.00&ops=true&factor%5Bops_hr%5D=0.00&factor%5Bops_p%5D=0.00&eqz=true&factor%5Beqz_hr%5D=0.00&factor%5Beqz_p%5D=0.00&zlh=true&factor%5Bzlh_hr%5D=0.00&factor%5Bzlh_p%5D=0.00&kpw=true&factor%5Bkpw_hr%5D=15.00&factor%5Bkpw_p%5D=110.00&ppw=true&factor%5Bppw_hr%5D=0.00&factor%5Bppw_p%5D=0.00&x25x=true&factor%5Bx25x_hr%5D=0.00&factor%5Bx25x_p%5D=0.00&fpw=true&factor%5Bfpw_hr%5D=16.00&factor%5Bfpw_p%5D=110.00&vh=true&factor%5Bvh_hr%5D=0.48&factor%5Bvh_p%5D=80.00&factor%5Bcost%5D=0.15&sort=Profitability24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate"
    driver.get(whatToMineLink)
    getProfitability = driver.find_element(
        By.CSS_SELECTOR, ".table-success > td:nth-child(8) > strong:nth-child(2)")
    profitability = usdToPln * float(getProfitability.text[1:])

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
        roi = float(gpuPrice[n].text[0 : -6]) / profitability
        print("RoI: " + str(round(roi, 2)) + " days")
        print(color.RED + "------------------------------------------------------------------------" + color.END)
        n += 1


def getRX6700():
    whatToMineLink = "https://whattomine.com/coins?aq_66xt=1&aq_69xt=0&aq_68xt=0&aq_68=0&aq_67xt=1&a_67xt=true&aq_vii=0&aq_5700xt=1&aq_5700=1&aq_5600xt=1&aq_vega64=0&aq_vega56=0&aq_3090=1&aq_38Ti=1&aq_3080=1&aq_38L=0&aq_37Ti=0&aq_3070=1&aq_37L=0&aq_3060Ti=0&aq_36TiL=0&aq_3060=0&aq_36L=0&aq_55xt8=0&aq_580=0&aq_570=1&aq_480=1&aq_470=1&aq_fury=0&aq_380=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=0&aq_1070Ti=0&aq_1070=0&aq_10606=0&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=48.00&factor%5Beth_p%5D=140.00&e4g=true&factor%5Be4g_hr%5D=48.00&factor%5Be4g_p%5D=140.00&zh=true&factor%5Bzh_hr%5D=54.00&factor%5Bzh_p%5D=120.00&cnh=true&factor%5Bcnh_hr%5D=0.00&factor%5Bcnh_p%5D=0.00&cng=true&factor%5Bcng_hr%5D=2000.00&factor%5Bcng_p%5D=130.00&cnr=true&factor%5Bcnr_hr%5D=0.00&factor%5Bcnr_p%5D=0.00&cnf=true&factor%5Bcnf_hr%5D=0.00&factor%5Bcnf_p%5D=0.00&eqa=true&factor%5Beqa_hr%5D=0.00&factor%5Beqa_p%5D=0.00&cc=true&factor%5Bcc_hr%5D=0.00&factor%5Bcc_p%5D=0.00&cr29=true&factor%5Bcr29_hr%5D=0.00&factor%5Bcr29_p%5D=0.00&ct31=true&factor%5Bct31_hr%5D=0.00&factor%5Bct31_p%5D=0.00&ct32=true&factor%5Bct32_hr%5D=0.00&factor%5Bct32_p%5D=0.00&eqb=true&factor%5Beqb_hr%5D=0.00&factor%5Beqb_p%5D=0.00&rmx=true&factor%5Brmx_hr%5D=0.00&factor%5Brmx_p%5D=0.00&ns=true&factor%5Bns_hr%5D=0.00&factor%5Bns_p%5D=0.00&al=true&factor%5Bal_hr%5D=80.00&factor%5Bal_p%5D=140.00&ops=true&factor%5Bops_hr%5D=24.00&factor%5Bops_p%5D=170.00&eqz=true&factor%5Beqz_hr%5D=0.00&factor%5Beqz_p%5D=0.00&zlh=true&factor%5Bzlh_hr%5D=36.00&factor%5Bzlh_p%5D=130.00&kpw=true&factor%5Bkpw_hr%5D=22.50&factor%5Bkpw_p%5D=160.00&ppw=true&factor%5Bppw_hr%5D=19.00&factor%5Bppw_p%5D=170.00&x25x=true&factor%5Bx25x_hr%5D=0.00&factor%5Bx25x_p%5D=0.00&fpw=true&factor%5Bfpw_hr%5D=24.00&factor%5Bfpw_p%5D=160.00&vh=true&factor%5Bvh_hr%5D=0.00&factor%5Bvh_p%5D=0.00&factor%5Bcost%5D=0.15&sort=Profitability24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate"
    driver.get(whatToMineLink)
    getProfitability = driver.find_element(
        By.CSS_SELECTOR, ".table-success > td:nth-child(8) > strong:nth-child(2)")
    profitability = usdToPln * float(getProfitability.text[1:])

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
        roi = float(gpuPrice[n].text[0 : -6]) / profitability
        print("RoI: " + str(round(roi, 2)) + " days")
        print(color.RED + "------------------------------------------------------------------------" + color.END)
        n += 1


def getRX6800():
    whatToMineLink = "https://whattomine.com/coins?aq_67xt=1&aq_69xt=0&aq_68xt=1&a_68xt=true&aq_68=1&aq_66xt=1&aq_vii=0&aq_5700xt=1&aq_5700=1&aq_5600xt=1&aq_vega64=0&aq_vega56=0&aq_3090=1&aq_38Ti=1&aq_3080=1&aq_38L=0&aq_37Ti=0&aq_3070=1&aq_37L=0&aq_3060Ti=0&aq_36TiL=0&aq_3060=0&aq_36L=0&aq_55xt8=0&aq_580=0&aq_570=1&aq_480=1&aq_470=1&aq_fury=0&aq_380=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=0&aq_1070Ti=0&aq_1070=0&aq_10606=0&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=64.00&factor%5Beth_p%5D=150.00&e4g=true&factor%5Be4g_hr%5D=64.00&factor%5Be4g_p%5D=150.00&zh=true&factor%5Bzh_hr%5D=90.00&factor%5Bzh_p%5D=150.00&cnh=true&factor%5Bcnh_hr%5D=0.00&factor%5Bcnh_p%5D=0.00&cng=true&factor%5Bcng_hr%5D=3300.00&factor%5Bcng_p%5D=180.00&cnr=true&factor%5Bcnr_hr%5D=0.00&factor%5Bcnr_p%5D=0.00&cnf=true&factor%5Bcnf_hr%5D=0.00&factor%5Bcnf_p%5D=0.00&eqa=true&factor%5Beqa_hr%5D=0.00&factor%5Beqa_p%5D=0.00&cc=true&factor%5Bcc_hr%5D=7.00&factor%5Bcc_p%5D=140.00&cr29=true&factor%5Bcr29_hr%5D=0.00&factor%5Bcr29_p%5D=0.00&ct31=true&factor%5Bct31_hr%5D=2.20&factor%5Bct31_p%5D=150.00&ct32=true&factor%5Bct32_hr%5D=0.90&factor%5Bct32_p%5D=150.00&eqb=true&factor%5Beqb_hr%5D=36.00&factor%5Beqb_p%5D=150.00&rmx=true&factor%5Brmx_hr%5D=0.00&factor%5Brmx_p%5D=0.00&ns=true&factor%5Bns_hr%5D=0.00&factor%5Bns_p%5D=0.00&al=true&factor%5Bal_hr%5D=110.00&factor%5Bal_p%5D=150.00&ops=true&factor%5Bops_hr%5D=44.00&factor%5Bops_p%5D=190.00&eqz=true&factor%5Beqz_hr%5D=0.00&factor%5Beqz_p%5D=0.00&zlh=true&factor%5Bzlh_hr%5D=0.00&factor%5Bzlh_p%5D=0.00&kpw=true&factor%5Bkpw_hr%5D=33.00&factor%5Bkpw_p%5D=200.00&ppw=true&factor%5Bppw_hr%5D=0.00&factor%5Bppw_p%5D=0.00&x25x=true&factor%5Bx25x_hr%5D=0.00&factor%5Bx25x_p%5D=0.00&fpw=true&factor%5Bfpw_hr%5D=35.00&factor%5Bfpw_p%5D=200.00&vh=true&factor%5Bvh_hr%5D=0.00&factor%5Bvh_p%5D=0.00&factor%5Bcost%5D=0.15&sort=Profitability24&volume=0&revenue=7d&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main&commit=Calculate"
    driver.get(whatToMineLink)
    getProfitability = driver.find_element(
        By.CSS_SELECTOR, ".table-success > td:nth-child(8) > strong:nth-child(2)")
    profitability = usdToPln * float(getProfitability.text[1:])

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
        roi = float(gpuPrice[n].text[0 : -6]) / profitability
        print("RoI: " + str(round(roi, 2)) + " days")
        print(color.RED + "------------------------------------------------------------------------" + color.END)
        n += 1


# Get Nvidia GPUs
getGTX1060()
getGTX1080TI()
getRTX2070()
getRTX3060TI()
# getRTX3070()
# getRTX3080()
# getRTX3080TI()
getRTX3090()

# Get AMD GPUs
# Scraping some GPUs might fail because of Allegro's rate limits. If you are looking for a particular model, then you can comment out other ones, to make the script work.
# Usually the script only fails to scrape two or three models. Nothing I can do about it.
getRX470()
getRX480()
getRX570()
getRX580()
# getRX5600XT()
# getRX5700()
# getRX6600XT()
# getRX6700()
# getRX6800()
