from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session
import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.onlinetrade.ru/catalogue/smartfony-c13/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Cookie": "spid=1688662180162_d33fdad048f6158c883194f0a3d28fcc_e03ctw7l0923pfbi; onlinetrade=0657217b4e9039a0d0a7fe30071fc44b; session_id=9edb28962f8f838f76bced9e6177bb00; user_city=1; user_c=14; views=2078646; _gcl_au=1.1.948486284.1688662183; _ym_uid=1688662183384020763; _ym_d=1688662183; spsn=1689305995361_7b2276657273696f6e223a22332e342e32222c227369676e223a226634613033333337336239636364316135393565626237653065386535623661222c22706c6174666f726d223a2257696e3332222c2262726f7773657273223a5b5d2c2273636f7265223a302e367d; spsc=1689306805519_54fa0d2ce984e97ac150264beee3128f_a5476469b72f558bb72e6aae99c6a060; _ym_isad=2"
}

page = requests.get(url=URL, headers=headers)
html = page.text

soup = bs(html, "html.parser")
items = soup.find_all("div", class_="indexGoods__item__name")
for item in items:
    print(item.get_text())

print("Hello")