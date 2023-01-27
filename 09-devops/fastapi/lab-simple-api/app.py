from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return { "message": "Hello Sparsh"}

@app.get("/customers")
async def customer_details() -> dict:
    return { "customer_name": "John Doe"}
