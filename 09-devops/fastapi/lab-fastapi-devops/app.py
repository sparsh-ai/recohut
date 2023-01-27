from fastapi import FastAPI
import uvicorn
from pydantic import  BaseModel

import os
import sys
from mangum import Mangum

import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))

stage = os.environ.get('STAGE', None)
root_path = f"/{stage}" if stage else "/"

app = FastAPI(title="DevOpsClass API",
        description='This API is an example of simple DevOps',
        version=1.0,
        redoc_url=None,
        root_path=root_path)

class ModelParams(BaseModel):
    years_of_experience: float

@app.get("/")
async def read_main():
    return {"msg": "Hello World!, Welcome to DevOps Class 101"}

# ##########################################################################################
# ## HANDLER ##
# ##########################################################################################

handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0')