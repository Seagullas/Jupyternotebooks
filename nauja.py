#!/bin/python3

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

url='https://www.aruodas.lt/butai/puslapis/2/'

driver.get(url)

time.sleep(20)

source= driver.page_source

bs= BeautifulSoup(source, 'html.parser')

Resultset= bs.find_all('div',{'class':'advert-flex'})

for skelbimas in Resultset:
    try:
        addres_element= skelbimas.find('div',{'class':'list-adress-v2'})
        tag=addres_element.find('h3').find('a',href=True)
        linkas= tag['href']
        # tekstą galim apsiekti ir per
        #.contents atributą
        tekstas= tag.contents #grąčžina lsit objektą su teksto gabaliukais
        f=''
        for i in tekstas:
            f= f + str(i).strip() #str garantuoja, kad būtų tekstas
        adresas= f.replace("<br/>",',')
        #tuo tarpu .text grąžina vientisą tekstą
        #tekstas = tag.text.strip() #string metodas, skirtas pašalinti tarpus iš pradžios bei pabaigos
        priceelement= skelbimas.find('span',{'class':'list-item-price-v2'})
        tekstas2=priceelement.contents
        f1= ''
        for i in tekstas2:
            f1=f1 + str(i).strip()
        kaina=f1.replace('</span>',",")

        priceelement1= skelbimas.find('span',{'class':'price-pm-v2'})
        tekstas3=priceelement1.contents
        f2= ''
        for i in tekstas3:
            f2=f2 + str(i).strip()
        kainakv=f2.replace('</span>',",").replace(' ',"")


        print('======SKELBIMAS=======')
        print(f'{linkas}\n {adresas}\n {kaina},\n {kainakv}')
    except:
        pass
driver.close()


# Jūsų užduotis:
# Iš printinti linką, adresą++, buto kainą, buto kainą už 1 kv metrą, vaizdas turi būti toks:
# ===SKELBIMAS===
# linkoas,++
# adreas++
# kaina++
# kaina už 1 kv metrą