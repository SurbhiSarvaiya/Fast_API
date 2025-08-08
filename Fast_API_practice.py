from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for request/response
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# GET endpoint with parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# POST endpoint to create an item
@app.post("/items/")
def create_item(item: Item):
    return {"item": item}
