from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Scraping():
    def __init__(self) -> None:
        self.site = 'https://www.kalunga.com.br/depto/smartphones-telefonia/smartphones/sansung/8/1190/4592'

        self.map = {
            'product': {
                'xpath': '/html/body/main/div/div[2]/div[3]/div[2]/div[2]/div/div/div[*x*]/div/div[2]/a/h2'
            },
            
            'price': {
                'xpath': '/html/body/main/div/div[2]/div[3]/div[2]/div[2]/div/div[1]/div[*x*]/div/div[2]/div[2]/span'
            }
        }

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def open(self):
        sleep(2)
        self.driver.get(self.site)
        sleep(2)

        product = self.driver.find_element(By.XPATH, self.map['product']['xpath'].replace("*x*", "1")).text.split(', ')

        price = self.driver.find_element(By.XPATH, self.map['price']['xpath'].replace("*x*", "1")).text.split()

        print(product[0])
        print(price[1])