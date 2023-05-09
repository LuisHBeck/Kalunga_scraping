from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class FastShopScraper:
    def __init__(self) -> None:
        self.url = "https://www.fastshop.com.br/web/c/4611686018425#PHONE#"
        self.map = {
            "title": {
                'xpath': "/html/body/app-root/div[1]/div[3]/app-category/div/div[4]/div[1]/div[2]/div[2]/app-product-list/div/app-product-item[#counter#]/div/a/div[3]/h3"
            },
            "price": {
                'xpath': "/html/body/app-root/div[1]/div[3]/app-category/div/div[4]/div[1]/div[2]/div[2]/app-product-list/div/app-product-item[#counter#]/div/a/div[3]/div[2]/app-price-v2/div/div[2]/span[1]"
            }
        }

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def open_site(self, phone=""):
        phone = "061003/samsung_galaxy"
        self.driver.get(self.url.replace('#PHONE#', phone))
        sleep(5)
        print("========== YEAR:", phone, "==========")
        counter = 1
        while True:
            try:
                title = self.driver.find_element(By.XPATH, self.map['title']['xpath'].replace('#counter#', str(counter))).text
                print(title, end=": ")
                price = self.driver.find_element(By.XPATH, self.map['price']['xpath'].replace('#counter#', str(counter))).text
                print(price, end=" ")
                counter += 1
            except Exception as e:
                print(e)
                break


web_scraper = FastShopScraper()
web_scraper.open_site()

# ---------------------

# https://www.fastshop.com.br/web/c/4611686018425  -  061003/samsung_galaxy
# https://www.fastshop.com.br/web/c/4611686018425  -  486503/iphone_
# https://www.fastshop.com.br/web/c/4611686018425  -  153535/motorola_moto
# https://www.fastshop.com.br/web/c/4611686018425  -  049504/zenfone_asus
# https://www.fastshop.com.br/web/c/4611686018425  -  159013/lg_smartphone
# https://www.fastshop.com.br/web/c/4611686018425  -  429004/xiaomi
# https://www.fastshop.com.br/web/c/4611686018425  -  494009/grupo_infinix
# https://www.fastshop.com.br/web/c/4611686018425  -  494008/grupo_positivo
