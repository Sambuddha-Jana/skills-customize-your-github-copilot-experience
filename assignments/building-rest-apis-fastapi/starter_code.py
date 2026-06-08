from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Simple Items API")


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float


# In-memory "database"
items_db = {
    1: {"id": 1, "name": "Widget", "description": "A useful widget", "price": 9.99},
    2: {"id": 2, "name": "Gadget", "description": "A fancy gadget", "price": 14.99},
}
next_id = max(items_db.keys()) + 1 if items_db else 1


@app.get("/items", response_model=List[Item])
def list_items():
    return list(items_db.values())


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = items_db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    global next_id
    item.id = next_id
    items_db[next_id] = item.dict()
    next_id += 1
    return items_db[item.id]


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    item.id = item_id
    items_db[item_id] = item.dict()
    return items_db[item_id]


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return None

# To run locally: uvicorn starter_code:app --reload
