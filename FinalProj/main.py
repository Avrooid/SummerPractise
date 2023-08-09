import threading
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import requests
import time
import json

from . import crud, models, schemas, parser
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def schedule_parser():
    head = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    headers_get = {
        'accept': 'application/json',
    }
    while True:
        print("Start parser!")
        prices = parser.parser()
        old_prices = requests.get('http://127.0.0.1:8000/prices', headers=headers_get).json()
        for old in old_prices:
            print(old)
        for price in prices:
            obj_not_in = True
            for old_price in old_prices:
                if price.get("name") == old_price["name"]:
                    obj_not_in = False
                    if price.get("price") != old_price["price"]:
                        temp_id = old_price["id"]
                        put_data = {
                            'price': price.get("price")
                        }
                        requests.put(f'http://127.0.0.1:8000/prices/{temp_id}', headers=head, json=put_data)
            json_data = {
                'name': price.get("name"),
                'price': price.get("price")
            }
            if obj_not_in:
                response = requests.post('http://127.0.0.1:8000/prices', headers=head, json=json_data)
        print("Finish parser!")
        time.sleep(20)


thread = threading.Thread(target=schedule_parser)
thread.start()


@app.post("/prices", response_model=schemas.PriceRead)
def create_price(price: schemas.PriceCreate, db: Session = Depends(get_db)):
    return crud.create_price(db=db, price=price)


@app.get("/prices", response_model=List[schemas.PriceRead])
def get_prices(db: Session = Depends(get_db)):
    return crud.get_prices(db)


@app.get("/prices/{price_id}", response_model=schemas.PriceRead)
def get_price(price_id: int, db: Session = Depends(get_db)):
    db_price = crud.get_price_by_id(db, price_id=price_id)
    if db_price is None:
        raise HTTPException(status_code=404, detail="Price not found")
    return db_price


@app.put("/prices/{price_id}", response_model=schemas.PriceRead)
def update_price(item: schemas.PriceUpdate, price_id: int, db: Session = Depends(get_db)):
    db_price = crud.get_price_by_id(db, price_id=price_id)
    if not db_price:
        raise HTTPException(status_code=404, detail="Price not found")
    return crud.update_price(db, item=item, price_id=price_id)


@app.delete("/prices/{price_id}", response_model=schemas.PriceRead)
def delete_price(price_id: int, db: Session = Depends(get_db)):
    db_price = crud.get_price_by_id(db, price_id=price_id)
    if not db_price:
        raise HTTPException(status_code=404, detail="Price not found")
    return crud.delete_price(db, price_id=price_id)
