from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from read import read_brand, read_price, read_only_brand
from kalunga import Scraping, brands, brands_list
from create import delete_all

screen = Tk()

brand = []

class Aplication():
    def __init__(self) -> None:
        self.window = screen
        self.screen()
        self.frames()
        self.buttons()
        self.labels()
        self.labels_db()
        self.clear_all()
        screen.mainloop()

    def screen(self):
        self.window.title('Kalunga Scraping')
        self.window.geometry('700x700')
        self.window.configure(background='#333333')
        self.window.resizable(False, False)

    def frames(self):
        self.frame0 = Frame(self.window, bg='#686868',
                            highlightthickness=0.5, highlightbackground='white')
        self.frame0.place(relx=0.03, rely=0.02, relwidth=0.94, relheight=0.12)

        self.frame1 = Frame(self.window, bg='#686868',
                            highlightthickness=0.5, highlightbackground='white')
        self.frame1.place(relx=0.03, rely=0.17, relwidth=0.94, relheight=0.12)

        self.frame2 = Frame(self.window, bg='#686868',
                            highlightthickness=0.5, highlightbackground='white')
        self.frame2.place(relx=0.03, rely=0.32, relwidth=0.94, relheight=0.65)

    def buttons(self):
        self.bt_scraping = Button(self.frame0, text='Scrapping', bg='#1f4788',
                                foreground='white', command=self.scraping)
        self.bt_scraping.place(relx=0.05, rely=0.25, relwidth=0.15, relheight=0.58)
        
        self.bt_plot = Button(self.frame0, text='Plot', bg='#1f4788',
                                foreground='white', command=self.plot)
        self.bt_plot.place(relx=0.8, rely=0.25, relwidth=0.15, relheight=0.58)
        
        self.bt_brand = Button(self.frame0, text='Select', bg='#1f4788',
                                foreground='white', command=self.show_models)
        self.bt_brand.place(relx=0.35, rely=0.25, relwidth=0.15, relheight=0.58)

    def labels(self):
        self.combobox = ttk.Combobox(self.frame0, values=brand)
        self.combobox.set('Select')
        self.combobox.place(relx=0.5, rely=0.25, relwidth=0.15, relheight=0.58)

    def labels_db(self):
        self.models_list = ttk.Treeview(self.frame2, height=3,
                                        columns=('col1', 'col2', 'col3', 'col4'))
        
        self.models_list.heading('#0', text='')
        self.models_list.heading('#1', text='id')
        self.models_list.heading('#2', text='Model')
        self.models_list.heading('#3', text='Price')

        self.models_list.column('#0', width=1)
        self.models_list.column('#1', width=50)
        self.models_list.column('#2', width=350)
        self.models_list.column('#3', width=200)

        self.models_list.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
        
        self.scroll_list = Scrollbar(self.frame2, orient='vertical')
        self.models_list.configure(yscrollcommand=self.scroll_list.set)
        self.scroll_list.place(relx=0.96 , rely=0.01, relwidth=0.04, relheight=0.98)

    def get_brand(self):
        self.brand_selected = self.combobox.get().lower()
        return self.brand_selected

    def show_models(self):
        self.clean()
        brand = self.get_brand()
        models_selected = read_brand(brand)

        for i in models_selected:
            self.models_list.insert('', 'end', values=i)

    def clean(self):
        self.models_list.delete(*self.models_list.get_children())

    def scraping(self):
        web = Scraping()
        web.open('firstpage','https://www.kalunga.com.br/depto/smartphones-telefonia/smartphones/8/1190?menuID=34&tipo=D', 'firstPage')

        web.open('nokia','https://www.kalunga.com.br/busca/1?q=smartphone-nokia', 'nokia')

        web.open('galaxy','https://www.kalunga.com.br/busca/1?q=smartphone-sansung', 'sansung')

        web.open('moto','https://www.kalunga.com.br/busca/1?q=smartphone-motorola', 'motorola')

        web.open('multi', 'https://www.kalunga.com.br/busca/1?q=smartphone-multig', 'multi')

        self.brand_list()

    def plot(self):
        table = self.get_brand()
        prices = read_price(table)
        brands = read_only_brand(table)

        fig, ax = plt.subplots()
        numbers = [str(num) for num in range(len(prices))]

        prices_new = []
        for price in prices:
            prices_new.append(*price)
        counts = [float((num).replace('.', '').replace(',', '.')) for num in prices_new]

        brand_new = []
        for brand in brands:
            brand_new.append(*brand)
        
        brand_foot = [brand.replace('Smartphone', '') for brand in brand_new]
        
        bar_colors = 'tab:blue'
        """ count is related to left column (prices) """
        ax.bar(brand_foot, counts, color=bar_colors)

        ax.set_title(f'Graphic representation')
        ax.set_ylabel('Amount of occurrences')

        plt.show()

    def brand_list(self):
        for i in brands_list:
            brand.append(i)

        self.labels()

    def clear_all(self):
        delete_all()
    

