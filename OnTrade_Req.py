import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.onlinetrade.ru/catalogue/noutbuki-c9/lenovo/noutbuk_lenovo_ideapad_l3_15itl6_82hl003brk-3053255.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
    "Cookie": "spid=1688662180162_d33fdad048f6158c883194f0a3d28fcc_e03ctw7l0923pfbi; spst=1688662180966_fb41eb7e7f6684494ace7a23f227f90a_b350434491ba66d4f19a71c5c6917fb3; spsn=1688662180162_7b2276657273696f6e223a22332e342e31222c227369676e223a226634613033333337336239636364316135393565626237653065386535623661222c22706c6174666f726d223a2257696e3332222c2262726f7773657273223a5b5d2c2273636f7265223a302e367d; spsc=1688662180162_d1bf73b2f0f730834a04693c7b3047b3_a5476469b72f558bb72e6aae99c6a060; onlinetrade=0657217b4e9039a0d0a7fe30071fc44b; session_id=9edb28962f8f838f76bced9e6177bb00; user_city=1; user_c=14; views=2078646; _gcl_au=1.1.948486284.1688662183; _ym_uid=1688662183384020763; _ym_d=1688662183; _ym_isad=2"
}

page = requests.get(url=URL, headers=headers)
html = page.text

print("OnlineTrade с requests+soup")

soup = bs(html, "html.parser")
title = soup.find("h1", itemprop="name")
print(title.get_text())

price = soup.find("span", itemprop="price")
price = price.get_text().replace(" ", "")
price = int(price)
print("Цена:", price)