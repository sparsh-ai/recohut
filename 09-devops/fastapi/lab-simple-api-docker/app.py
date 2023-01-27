import os
from fastapi import FastAPI

import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))

app = FastAPI(version="1.0", root_path="/")

@app.get("/")
async def read_main():
    return {"msg": "Simple FastAPI"}