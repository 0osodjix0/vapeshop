from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI


@app.get("/")
def read_root():
    return {"Hello": "World"}
app = FastAPI()

# База товаров
products = [
    {"id": 1, "name": "Vape X100", "price": 25.99, "description": "Мощный вейп с отличным вкусом"},
    {"id": 2, "name": "Liquid Berry", "price": 9.99, "description": "Фруктовый микс для заправки"},
]

# Модель товара
class Product(BaseModel):
    name: str
    price: float
    description: str

# Получение списка товаров
@app.get("/products")
def get_products():
    return products

# Добавление нового товара
@app.post("/products")
def add_product(product: Product):
    new_product = {"id": len(products) + 1, **product.dict()}
    products.append(new_product)
    return new_product

# Запуск сервера
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)