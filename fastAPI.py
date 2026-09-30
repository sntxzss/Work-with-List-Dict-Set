from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
  name: str
  price: float
  is_offer: bool = None

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
  return {"item_id": item_id, "query_search": q}

@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
  return {
      "message": "Товар успішно створено!",
      "created_item": item,  
  }