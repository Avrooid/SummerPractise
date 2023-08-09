import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re

URL = "https://www.ozon.ru/product/pesochnitsa-derevyannaya-564916648/?advert=9_Pz3RjN2l5x-SB23b9m1uM27Zo_kNzu-CC0pZxHkLx6WrMsyb4lpjrb-iWQdFd5LIhoD5vhVtQUHvpZq7DjDlLgVD2NbIt_85zF15LaWANjZKwm4iDLpU7VrYOcKNJIUNtKHqZNE8PB5uWJmLEI-oBZPLxW1pROj2shURCdigGVA5WXEi1CL51ME_luSjOloK_Ggm-8QqU&avtc=1&avte=2&avts=1688665782&sh=OD0eC1DOlg"

driver = webdriver.Firefox()
driver.get(URL)
time.sleep(3)

html = driver.page_source

driver.close()
driver.quit()

print("Ozon с requests+soup")

soup = bs(html, "html.parser")
title = soup.find("h1", class_="z8k")
print(title.get_text())

price = soup.find("span", class_="k0z")
price = re.sub(r'[^\d,.]', '', price.get_text())
price = int(price)
print("Цена:", price)