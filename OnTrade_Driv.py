import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs

URL = "https://www.onlinetrade.ru/catalogue/noutbuki-c9/lenovo/noutbuk_lenovo_ideapad_l3_15itl6_82hl003brk-3053255.html"

driver = webdriver.Firefox()
driver.get(URL)
time.sleep(3)

html = driver.page_source

driver.close()
driver.quit()

print("OnlineTrade с webdriver+soup")

soup = bs(html, "html.parser")
title = soup.find("h1", itemprop="name")
print(title.get_text())

price = soup.find("span", itemprop="price")
price = price.get_text().replace(" ", "")
price = int(price)
print("Цена:", price)