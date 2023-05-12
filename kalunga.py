from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from create import create, create_table
import pandas as pd

brands = set()
brands_list = []

index = []
model = []
price_v = []

class Scraping():
    def __init__(self) -> None:

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
                'xpath': '/html/body/main/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div[*x*]/div/div[2]/div[2]/span',

                'xpath2': '/html/body/main/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div[*x*]/div/div[2]/div/span'
            }
            },

            'nokia': {
                'product': {
                    'xpath': '/html/body/main/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div[*x*]/div/div[2]/a/h2'
                },
                'price': {
                    'xpath':'/html/body/main/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div[*x*]/div/div[2]/div[2]/span',

                    'xpath2': '/html/body/main/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div[*x*]/div/div[2]/div/span'
                }
            },

            'motorola': {
                'product': {
                    'xpath': '/html/body/main/div[2]/div[2]/div/div[3]/div[1]/div[1]/div[*x*]/div/div[2]/a/h2'
                },

                'price': {
                    'xpath': '/html/body/main/div[2]/div[2]/div/div[3]/div[1]/div[1]/div[*x*]/div/div[2]/div[2]/span'
                }
            },

            'multi': {
                'product': {
                    'xpath': '/html/body/main/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div[*x*]/div/div[2]/a/h2'
                },

                'price': {
                    'xpath': '/html/body/main/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div[*x*]/div/div[2]/div[2]/span' 
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

        create_table(table)
        
        brands_list.append(table)

        for x in range(1, 11):
            try:
                product = self.driver.find_element(By.XPATH, self.map[page]['product']['xpath'].replace("*x*", f'{x}')).text.split(', ')
                
                product = product[0]
                # print(product)

                price = self.driver.find_element(By.XPATH, self.map[page]['price']['xpath'].replace("*x*", f'{x}')).text.split()
                
                price = price[1].replace('.', '').replace(',', '.')
                # print(price)

                if product[0] in 'Smartphone':
                    create(table, product, price)

                if page == 'firstPage':
                    model.append(product)
                    price_v.append(price)
                    smartphones = {
                    'model': model,
                    'price': price_v
                    }

                    dataframe = pd.DataFrame(smartphones)
                    dataframe.to_excel('./xlsx_archives/Products.xlsx', sheet_name=table, )
                    dataframe.to_csv('./xlsx_archives/Products.csv', sep=";")
                    
            except:
                print(f'Error #{x}')
        

        