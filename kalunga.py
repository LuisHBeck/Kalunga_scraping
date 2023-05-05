from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from create import create

class Scraping():
    def __init__(self) -> None:
        # self.site = 'https://www.kalunga.com.br/depto/smartphones-telefonia/smartphones/sansung/8/1190/4592'

        # self.site = 'https://www.kalunga.com.br/depto/smartphones-telefonia/smartphones/8/1190?menuID=34&tipo=D'

        self.map = {
            'firstPage': {
                'product': {
                'xpath': '/html/body/main/div/div[2]/div[3]/div[2]/div[2]/div/div/div[*x*]/div/div[2]/a/h2'
            },
            
            'price': {
                'xpath': '/html/body/main/div/div[2]/div[3]/div[2]/div[2]/div/div[1]/div[*x*]/div/div[2]/div[2]/span'
            }
            },
            
            'sansung': {
                'product': {
                'xpath': '/html/body/main/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div[*x*]/div/div[2]/a/h2'
            },
            
            'price': {
                'xpath': '/html/body/main/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div[*x*]/div/div[2]/div[2]/span'
            }
            },

            'nokia': {
                'product': {
                    'xpath': '/html/body/main/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div[*x*]/div/div[2]/a/h2'
                },
                'price': {
                    'xpath':'/html/body/main/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div[*x*]/div/div[2]/div[2]/span'
                }
            }
        }

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def open(self, table, site, page):
        sleep(2)
        self.driver.get(site)
        sleep(2)

        for x in range(1, 11):
            try:
                product = self.driver.find_element(By.XPATH, self.map[page]['product']['xpath'].replace("*x*", f'{x}')).text.split(', ')
                
                product = product[0]
                print(product)

                price = self.driver.find_element(By.XPATH, self.map[page]['price']['xpath'].replace("*x*", f'{x}')).text.split()
                
                price = price[1]
                print(price)

                create(table, product, price)
            except:
                print(f'Error #{x}')