import re
import requests
from bs4 import BeautifulSoup as bs
from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

URL = "https://www.sima-land.ru/igrushki/letnie-tovary/detskie-myachi/svetovye-myachi/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Cookie": "abSegment=I; abVersion=2; oko-uid=q24XCpZA0IQM3lGj; hasCookiesAgree=1; _gcl_au=1.1.24652279.1689307906; settlement_id=27503892; user_settings=%7B%22sort%22%3A%22price%22%2C%22per_page%22%3A20%2C%22currency%22%3A%22RUB%22%2C%22viewtype%22%3A%22list%22%2C%22mode%22%3A%22server%22%7D; userSettings=f5e22b2516a51a4d0725ed48b7982af1d640b6a6a56639b72159d9f8f8bad13fa%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22userSettings%22%3Bi%3A1%3Bs%3A107%3A%22%7B%22sort%22%3A%22price%22%2C%22per_page%22%3A20%2C%22currency%22%3A%22RUB%22%2C%22viewtype%22%3A%22list%22%2C%22viewtypes%22%3A%5B%5D%2C%22sorts%22%3A%5B%5D%2C%22mode%22%3A%22server%22%7D%22%3B%7D; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=7ec579f6-4651-4bea-b70c-1073e0d135f2; _ga_BDRVG0GET6=GS1.1.1691419138.3.0.1691419138.60.0.0; _ga=GA1.2.720976080.1689307906; _ga_6EH1EVKLTZ=GS1.1.1691419138.3.0.1691419138.60.0.0; district_id=537; flocktory-uuid=6d4c51c4-4d4c-4a3f-92a5-8181b8391568-0; tmr_lvid=d1a4931ad66440286933bcb763c7131a; tmr_lvidTS=1689307908200; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; NEWSIMALAND=a870c495ec279512fee5e3497fa8383d; city_id=7996abe1aa6804a09dd3dfcc6e301441df3d1d77e659c2c66a40a95eaf88c7f7a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%22city_id%22%3Bi%3A1%3Bi%3A27503892%3B%7D; country=50fa73c1717e928f15414ffc679f880ea767aa7cd87af488d2b810a15b6312b1a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%22country%22%3Bi%3A1%3Bs%3A2%3A%22RU%22%3B%7D; EXPRESS=hoiwuh36; _gid=GA1.2.371079829.1691419139; _dc_gtm_UA-5187674-1=1; _gat_UA-5187674-1=1; mindboxDeviceUUID=6d4509e4-eaf8-4db4-8bbf-66714d29c8de; directCrm-session=%7B%22deviceGuid%22%3A%226d4509e4-eaf8-4db4-8bbf-66714d29c8de%22%7D; tmr_detect=0%7C1691419141281"
}


def parser():
    page = requests.get(url=URL, headers=headers)
    html = page.text

    soup = bs(html, "html.parser")
    items = soup.find_all("div", class_="m4OA1R HWFMiU f9d3Zv jCkt4I catalog__item")
    products = []
    for item in items:
        name = item.find("span", class_="jBE82l")
        name = name.get_text()
        price = item.find("span", class_="ZQrSS6")
        price = re.sub(r'[^\d,.]', '', price.get_text())
        price = int(price)
        products.append(
            {
                "name": name,
                "price": price
            }
        )
        print(name, price)
    return products
