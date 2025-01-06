from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Form, status, HTTPException

from app import schemas
from db import get_db
from db.models import Product


router = APIRouter(tags=["Products"])

# TODO: writing json api for posts beside (or instead) of params


@router.post("/product/", response_model=schemas.ProductRead, status_code=status.HTTP_201_CREATED)
def add_product(
    product_id: str = Form(description="Product ID"),
    name: str = Form(description="Product Name"),
    stock: int = Form(1, description="Product Stock"),
    minimum_stock: int = Form(3, description="Product Minimum Stock"),
    db: Session = Depends(get_db)
):
    db_product = db.query(Product).filter(product_id == Product.id).first()
    if db_product:
        raise HTTPException(status_code=404, detail="Product already exists.")
    product_data = schemas.ProductCreate(
        id=product_id,
        name=name,
        stock=stock,
        minimum_stock=minimum_stock,
    )
    db_product = Product(**product_data.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.get("/product/{product_id}", response_model=schemas.ProductRead)
def get_product(product_id: str, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(product_id == Product.id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.put("/product/{product_id}", response_model=schemas.ProductRead)
def update_product(
    product_id: str,
    name: str = Form(None, description="Product Name"),
    stock: int = Form(None, description="Product Stock"),
    minimum_stock: int = Form(None, description="Product Minimum Stock"),
    db: Session = Depends(get_db)
):
    db_product = db.query(Product).filter(product_id == Product.id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    if name is not None:
        db_product.name = name
    if stock is not None:
        db_product.stock = stock
    if minimum_stock is not None:
        db_product.minimum_stock = minimum_stock
    db.commit()
    return db_product


@router.delete("/product/{product_id}")
def delete_product(product_id: str, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(product_id == Product.id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"success": True, "message": "Product deleted"}


@router.put("/product/stock/{product_id}", response_model=schemas.ProductRead)
def change_product_stock(
    product_id: str,
    amount: int = Form(-1, description="Positive or Negative to change"),
    db: Session = Depends(get_db)
):
    db_product = db.query(Product).filter(product_id == Product.id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product.stock += amount
    db.commit()
    return db_product


@router.get("/products/")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(Product).all()
    return db_products


@router.get("/product/low_stocks/")
def get_low_stock_products(db: Session = Depends(get_db)):
    db_low_stock_products = db.query(Product).filter(Product.stock <= Product.minimum_stock).all()
    return db_low_stock_products


@router.get("/product/predict_stock_depletion/{product_id}")
def get_predict_stock_depletion(product_id: str, daily_sale: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(product_id == Product.id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    days_left = db_product.stock // daily_sale
    return {"warning": days_left <= 7, "days_left": days_left, "product": db_product}
