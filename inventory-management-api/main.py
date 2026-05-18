from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

database_models.Base.metadata.create_all(bind=engine)

products = [
    Product(id=1, name="samsung A72", description="128GB storage, 8GB RAM", price=250, quantity=6),
    Product(id=2, name="lenovo LOQ 15", description="512GB storage, 18GB RAM", price=800, quantity=18),
    Product(id=3, name="iPhone 13", description="128GB, A15 Bionic chip, Dual camera", price=650, quantity=10),
    Product(id=4, name="MacBook Air M2", description="256GB SSD, 8GB RAM, Apple M2 chip", price=1100, quantity=5),
    Product(id=5, name="Dell XPS 13", description="512GB SSD, 16GB RAM, Intel i7", price=1200, quantity=7),
    Product(id=6, name="Sony WH-1000XM5", description="Noise cancelling wireless headphones", price=350, quantity=15),
    Product(id=7, name="Logitech MX Master 3S", description="Wireless ergonomic mouse", price=120, quantity=25),
    Product(id=8, name="iPad Air", description="10.9-inch display, Apple M1 chip", price=700, quantity=9)
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()

    count = db.query(database_models.Product).count()

    if count ==0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))

        db.commit()

init_db()

@app.get("/")
def greet():
    return "welcome!"

@app.get("/products")
def get_all(db: Session = Depends(get_db)):
    
    db_products = db.query(database_models.Product).all()
    
    return db_products

@app.get("/products/{id}")
def get_products_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    raise HTTPException(status_code=404, detail=f"product not found")

@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return {"message": "product updated successfully"}
    raise HTTPException(status_code=404, detail=f"product not found")

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        product_name = db_product.name
        db.delete(db_product)
        db.commit()
        return {"message": f"{product_name} deleted successfully"}
    raise HTTPException(status_code=404, detail=f"product not found")