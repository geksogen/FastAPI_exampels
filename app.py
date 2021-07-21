from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test/{item_id}")
async def read_item(item_id: int):
    print(item_id)
    return {"item_id": item_id}


@app.post("/items/")
async def create_item(item: Item):
    return item


#uvicorn.run(app, host="0.0.0.0", port="8080")