from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel
import secrets

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None


app = FastAPI()

security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "otus")
    correct_password = secrets.compare_digest(credentials.password, "otus123")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/")
def read_root(credentials: HTTPBasicCredentials = Depends(get_current_username)):
    return {"Aloha": "Men :::::::::!)"}

@app.get("/test/{item_id}")
async def read_item(item_id: int, credentials: HTTPBasicCredentials = Depends(get_current_username)):
    print(item_id)
    return {"item_id": item_id}

@app.get("/check")
def hello():
    return "Hello World"

@app.post("/items/")
async def create_item(item: Item, credentials: HTTPBasicCredentials = Depends(get_current_username)):
    return item


#uvicorn.run(app, host="0.0.0.0", port="8080")