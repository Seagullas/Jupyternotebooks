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

#surinkite iš puslapių nuo 2 iki 11-to butų skelbimus ir tokią informaciją - kaina, kaina už 1 kv metrą, adresas, plotas, kambarių kiekis. 
# šiuos duomenis eksportuokite į csv failą, skirtukas turi būti ;.++
#suraskite, kiek iš atrinktų butų buvo pagal kainą pigūs, brangūs, neįperkami. 
# Kriterijus - 1 kv metro kaina iki 1 VDu - pigūs, iki 3 VDU - brangūs, daugiau nei 3 VDU - neįperkami.
#pavaizduokite su boxplotais kainų už 1 kv pasiskirstymą nuo kambarių skaičiaus.
#Pavaizduokiet tokią informaciją: atrinktų butų kainų pasiskirstymą tarp miestų.
#pavaizduokite tokią informaciją - kiek buvo sklebimų per skirtingus miestus jūsų atrankoje?

skelbimaiall =[]
psl= [2,3]
for puslapis in psl:
    url=f'https://www.aruodas.lt/butai/puslapis/{puslapis}/'
    driver.get(url)
    time.sleep(20)
    source=driver.page_source
    bs=BeautifulSoup(source,'html.parser')
    Resultset= bs.find_all('div',{'class':'advert-flex'})
    tt= pd.DataFrame()
    adr=[]
    kain=[]
    kvm=[]
    plot=[]
    kamb=[]
    l=[]
    for skelbimas in Resultset:
        try:
            addres_element= skelbimas.find('div',{'class':'list-adress-v2'})
            tag=addres_element.find('h3').find('a',href=True)
            linkas= tag['href']
            tekstas= tag.contents #grąčžina lsit objektą su teksto gabaliukais
            f=''
            for i in tekstas:
                f= f + str(i).strip() #str garantuoja, kad būtų tekstas
            adresas= f.replace("<br/>",',')
            adr.append(adresas)

            priceelement= skelbimas.find('span',{'class':'list-item-price-v2'})
            tekstas2=priceelement.contents
            f1= ''
            for i in tekstas2:
                f1=f1 + str(i).strip()
            kaina=f1.replace('</span>',",")
            kain.append(kaina)

            priceelement1= skelbimas.find('span',{'class':'price-pm-v2'})
            tekstas3=priceelement1.contents
            f2= ''
            for i in tekstas3:
                f2=f2 + str(i).strip()
            kainakv=f2.replace('</span>',",").replace(' ',"")
            kvm.append(kainakv)

            priceelement2= skelbimas.find('div',{'class':'list-AreaOverall-v2 list-detail-v2'})
            tekstas4=priceelement2.contents
            f3= ''
            for i in tekstas4:
                f3=f3 + str(i).strip()
            plotas=f3.replace("<br/>",',')
            plot.append(plotas)

            priceelement3= skelbimas.find('div',{'class':'list-RoomNum-v2 list-detail-v2'})
            tekstas5=priceelement3.contents
            f4= ''
            for i in tekstas5:
                f4=f4 + str(i).strip()
            kambariai=f4
            kamb.append(kambariai)
            print(adr, kain, kvm, plot, kamb)
            # tt['skelbimas']=adresas, kaina, kainakv, plotas, kambariai
            # tt.to_csv('Arinfo4.csv', sep= ';',mode='a')
            # print('======SKELBIMAS=======')
            # print(f'{adresas}\n {kaina},\n {kainakv},\n {plotas},\n {kambariai}')
            tt['adresas']= adr
            tt['kaina']= kain
            tt['kainakvm']= kvm
            tt['plotas']=plot
            tt['kambariusk']=kamb
            tt.to_csv('Aruodorez2.csv',sep=';',mode='a')
        except Exception as klaida:
            print(klaida)
        tt['adresas']= adr
        tt['kaina']= kain
        tt['kainakvm']= kvm
        tt['plotas']=plot
        tt['kambariusk']=kamb
        tt.to_csv('Aruodorez2.csv',sep=';',mode='a')
print(kain)
driver.close()

    # adr=[]
    # kain=[]
    # kvm=[]
    # plot=[]
    # kamb=[]
