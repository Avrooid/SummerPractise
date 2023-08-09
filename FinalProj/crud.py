from . import models, schemas
from sqlalchemy.orm import Session


def get_price_by_name(db: Session, name: str):
    return db.query(models.Price).filter(models.Price.name == name).first()


def get_price_by_id(db: Session, price_id: int):
    return db.query(models.Price).filter(models.Price.id == price_id).first()


def create_price(db: Session, price: schemas.PriceCreate):
    db_price = models.Price(
        name=price.name,
        price=price.price
    )
    db.add(db_price)
    db.commit()
    db.refresh(db_price)
    return db_price


def get_prices(db: Session):
    return db.query(models.Price).all()


def update_price(db: Session, item: schemas.PriceUpdate, price_id: int):
    record = get_price_by_id(db, price_id)
    record.price = item.price
    db.commit()
    return record


def delete_price(db: Session, price_id: int):
    db_item = get_price_by_id(db, price_id=price_id)
    db.delete(db_item)
    db.commit()
    return db_item
