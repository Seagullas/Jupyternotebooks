import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

import time
import selenium
#import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

opcijos = Options()
opcijos.add_argument('--incognito')
# opcijos.add_argument('--headless') #paleidžia naršyklę jos neatidarant kaip buvo su incognito

# driver = uc.Chrome(options=opcijos)
driver = webdriver.Chrome(options=opcijos)


puslapio_nr = [2,3,4,5,6]
kurotipas = []
variklis = []
pavarudeze = []
rida = []
tipas = []
vieta= []
data=[]
for puslapis in puslapio_nr:
    url = f'https://m.autoplius.lt/skelbimai/naudoti-automobiliai?qt=&page_nr={puslapis}'
    opcijos = Options()
    driver = webdriver.Chrome(options=opcijos)
    driver.get(url)
    time.sleep(20)
    source = driver.page_source
    data = []
    bs = BeautifulSoup(source, 'html.parser')
    ResultSet = bs.find_all('div', {'class':'description'})
    print(len(ResultSet))
    for skelbimas in ResultSet:
        try:
            price_element= skelbimas.find('div', {'class':'pricing-container'})
            tag = price_element.find('strong')
            kaina = tag.contents[0]

            kuras_element= skelbimas.find('div', {'class':'item-parameters'})
            #tag1 = parametrai_element.find('span')
            kuras =kuras_element.contents[1]

            variklis_element= skelbimas.find('div', {'class':'item-parameters'})
            #tag1 = parametrai_element.find('span')
            varikl =variklis_element.contents[3]

            deze_element= skelbimas.find('div', {'class':'item-parameters'})
            #tag1 = parametrai_element.find('span')
            pavaros =deze_element.contents[5]

            rid_element= skelbimas.find('div', {'class':'item-parameters'})
            #tag1 = parametrai_element.find('span')
            ridas =rid_element.contents[7]

            tipas_element= skelbimas.find('div', {'class':'item-parameters'})
            #tag1 = parametrai_element.find('span')
            tips =tipas_element.contents[9]

            viet_element= skelbimas.find('div', {'class':'item-parameters'})
            #tag1 = parametrai_element.find('span')
            viet =tipas_element.contents[11]



            f = ''
            for i in kaina:
                f = f + i.strip()
            kaina = f.replace(' €', '').replace('€','')

            f1 = ''
            for a in kuras:
                f1 = f1 + str(a).strip()
            kurs = f1

            f2 = ''
            for a in varikl:
                f2 = f2 + str(a).strip()
            varik = f2.replace(' ','')

            f3 = ''
            for a in pavaros:
                f3 = f3 + str(a).strip()
            pavardeze = f3

            f4 = ''
            for a in ridas:
                f4 = f4 + str(a).strip()
            ridos = f4.replace(' km','').replace(' ','')

            f5 = ''
            for a in tips:
                f5 = f5 + str(a).strip()
            tipasas = f5

            f6 = ''
            for a in viet:
                f6 = f6 + str(a).strip()
            vietove = f6


            d={'kaina;': kaina, 'kuro tipas;': kurs, 'variklis;': varik,'pavaru deze;': pavardeze,'rida;':ridos,'tipas;':tipasas,'vietove;':vietove}
            data.append(d)
            print(d)

        except Exception as klaida:
            print(klaida)
    try:
        df = pd.read_csv('rez3.csv')
        append_mode = 'a'  # Append mode
    except FileNotFoundError:
        # If file doesn't exist, create it with the header
        df = pd.DataFrame(columns=data[0].keys())
        df.to_csv('rez3.csv', index=False)
        append_mode = 'w'  # Write mode
    df = pd.DataFrame(data=data)
    df.to_csv('rez3.csv',mode='a', header=False, index=False, sep=';')
driver.close()