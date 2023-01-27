from fastapi import FastAPI

app = FastAPI()

sales = {
    1: {"item": "tin", "unit_price": 4, "quantity": 5},
    2: {"item": "2 liters", "unit_price": 15, "quantity": 5},
    3: {"item": "12 fl oz", "unit_price": 10, "quantity": 5},
    4: {"item": "mini tin", "unit_price": 2, "quantity": 5},
}


@app.get("/")
def home():
    return {"Sales": len(sales)}


@app.get("/sales/{sale_id}")
def sale_get(sale_id: int):
    if sale_id in sales:
        return sales[sale_id]
    else:
        return {"Error: Sale ID not found!"}