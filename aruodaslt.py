import selenium
# import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time # dėl sleep komandos


opcijos = Options()
opcijos.add_argument('--incognito')

# driver = uc.Chrome(options=opcijos)
driver = webdriver.Chrome(options=opcijos)

url = "https://www.kaunodiena.lt"

driver.get(url)
time.sleep(3)
pav= pd.DataFrame()
source = driver.page_source # pasiimam puslapio html kodą

bs = BeautifulSoup(source, 'html.parser') #teoriškai išparsiname puslapio html
resultset= bs.find_all('a',{'class':'articles-list-title'})
z=[]
for elementas in resultset:
    print('::ELEMENTAS::')
    print(elementas)
    print(elementas['href']) #href- hyperreference. ['href'] iš atrinktos klasės leidžia gauti link'ą
    print(elementas.text) #išvestyje pasiekiame elemente esantį tekstą. Šiuo atveju- straipsnio pavadinimą
    z.append(elementas.text)

pav['pavadinimas']=z
pav.to_csv('kaunodiena.csv', sep= ';')
#driver.close()