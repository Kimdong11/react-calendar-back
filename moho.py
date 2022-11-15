import requests
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

from time import sleep



def make_value(string) : 
    navailable = string.find("불")
    only_check_out = string.find("체크아웃")
    if navailable != -1 :
        return string[navailable : navailable + 2]
    elif only_check_out != -1 :
        return "체크아웃" 
    else :
        return "가능"
        
def make_key(string) :
    date = string.find("2022")
    if date != -1 :
        full_date = string[date+8 : date + 10] + "-" + string[date + 5 : date + 7] + "-" + string[date : date + 4] 
        return full_date
    else :
        return "temp"


url = "https://www.airbnb.co.kr/rooms/742349141243284218?adults=1&source_impression_id=p3_1668249908_8PelW3RZv7xYEViD&guests=1"

options = webdriver.ChromeOptions()
options.add_argument("headless")
browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get(url)
sleep(2)
html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')

tds1 = soup.select("#site-content > div > div:nth-child(1) > div:nth-child(3) > div > div._16e70jgn > div > div:nth-child(6) > div > div:nth-child(2) > div > div._sk02b4 > div > div:nth-child(1) > div > div > div > div > div._14676s3 > div._1foj6yps > div > div._1lds9wb > div > table > tbody > tr > td")
tds2 = soup.select("#site-content > div > div:nth-child(1) > div:nth-child(3) > div > div._16e70jgn > div > div:nth-child(6) > div > div:nth-child(2) > div > div._sk02b4 > div > div:nth-child(1) > div > div > div > div > div._14676s3 > div._1foj6yps > div > div:nth-child(3) > div > table > tbody > tr > td")

datas = []
datas2 = []
remove_set = {"temp" : "가능"}


for td in tds1 :
    datas.append({make_key(str(td)) : make_value(str(td))})

for td in tds2 :
    datas2.append({make_key(str(td)) : make_value(str(td))})

data = [i for i in datas if  i != remove_set]
data2 = [i for i in datas2 if i != remove_set]

data = data + data2

print(data)

