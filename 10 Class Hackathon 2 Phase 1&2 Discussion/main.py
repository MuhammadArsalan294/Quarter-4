from fastapi import FastAPI
from fastapi import Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Field, SQLModel, create_engine, Session
from typing import Optional, Generator
import os
from dotenv import load_dotenv #  uv add python-dotenv


load_dotenv() # Ye .env ki file sy atey hain

DATABASE_URL = os.getenv("DATABASE_URL") # Yaha get kia env ko
engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    """Create the database and tables."""
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    """Get database session"""
    with Session(engine) as session:
        yield session

app = FastAPI() # Ye Object bna rha / instance bna rha

@app.on_event("startup") # Startup event hai 
def on_startup():
    create_db_and_tables()   # Ye aik function hai jo database or tables bnaye ga


# SQL MODEL CLASS

class Product(SQLModel, table=True): # Yaha inheritance ho rhi kyu ky aik class ky andr dusri class ka name a rha # Class kia krey gi database ka table bnaye gi or table mein hon gay column Yani nechy attributes jo hain wo columns ky name hain
    id: int | None = Field(default=None, primary_key=True) # Field yanic 1 number py focus primary key yani aik unique number
    name: str
    price: float
    in_stock: bool


class Blog(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


products_db = [
    {"id": 1, "name": "Laptop", "price": 999.99, "in_stock": True},
    {"id": 2, "name": "Smartphone", "price": 499.99, "in_stock": False},
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/products")
async def read_root():
    return products_db


"""
Legacy in-memory create endpoint (kept for reference).
Commented out to avoid duplicate route definitions.
Beginner note: this version appends to a Python list only,
so data disappears when the server restarts.
"""
# @app.post("/products")
# async def create_products(product: Product):
#     print(type(product))
#     products_db.append(product.dict())
#     return {"message": "Products created successfully (in-memory)."}

# Database main code insert kar rhy 
@app.post("/products")
def create_product(product: Product, session: Session = Depends(get_session)): # Jab bhi database sy bt kren gay means kuch add ya delete krein gay gay tw aik session perform kar ky hota hai ye yani session create hota hai es ki zarorat hoti hai Dpends means agar user ka session create hoga tw he wo database sy bt krey ga
    # Beginner-friendly: insert into DB using SQLModel session
    # Ensure id is None so DB can auto-generate if configured
    product.id = None
    session.add(product)
    session.commit()  # write changes
    session.refresh(product)  # get auto-generated fields like id
    return {"message": "Product created successfully.", "product": product}

    
 
    return {"message": "Products created successfully."}


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    global products_db
    new_products = []
    for product in products_db:
        if product["id"] != product_id:
            new_products.append(product)
    products_db = new_products
    return {"message": "Product deleted successfully."}

@app.put("/products/{product_id}")
async def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products_db):
        if product["id"] == product_id:
            products_db[index] = updated_product.dict()
            return {"message": f"{updated_product.name} updated successfully."}
    return {"message": "Product not found."}

