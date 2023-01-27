from typing import List
import os

from fastapi import Depends, FastAPI, HTTPException, status, Security, BackgroundTasks
from fastapi.security.api_key import APIKeyQuery, APIKeyHeader, APIKey
from passlib.context import CryptContext
from pydantic import BaseModel

from src.model import MyClassificationModel

import src.handle as handle


root_dir = '../../data/artifacts'


app = FastAPI(title="Classification API", 
              description="Classifies the text reviews", 
              version="1.0")


##########################################################################################
## AUTH CODE ##
##########################################################################################


API_KEY_HASH = "<api_key>"
API_KEY_NAME = "access_token"

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

async def get_api_key(
    api_key_query: str = Security(api_key_query),
    api_key_header: str = Security(api_key_header),
):
    print(api_key_query)
    print(api_key_header)
    
    if api_key_query is not None and verify_password(api_key_query, API_KEY_HASH):
        return api_key_query
    elif api_key_header is not None and verify_password(api_key_header, API_KEY_HASH):
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials"
        )


##########################################################################################
## APP CODE ##
##########################################################################################


class body_classify_text(BaseModel):
    user_id : str
    product_ids : List
    weights : dict = None
    return_df : bool = False

@app.get("/")
async def read_main(background_tasks: BackgroundTasks):
    return {"msg": "Text Classification API"}


@app.post('/classify_text')
async def classify_text(data: body_classify_text, api_key: APIKey = Depends(get_api_key)):
    predictions = handle.model_classify_text.predict(user_id = data.user_id, 
                                                            product_ids = data.product_ids)
    return {"predictions": predictions}


##########################################################################################
## HANDLER ##
##########################################################################################

if __name__ == '__main__':
    uvicorn.run(app)