from typing import Optional, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Items API")


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


ITEMS: Dict[int, Item] = {}
_next_id = 1


def _get_next_id() -> int:
    global _next_id
    nid = _next_id
    _next_id += 1
    return nid


@app.get("/items")
def list_items():
    return [{"id": i, **ITEMS[i].dict()} for i in ITEMS]


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in ITEMS:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **ITEMS[item_id].dict()}


@app.post("/items", status_code=201)
def create_item(item: Item):
    item_id = _get_next_id()
    ITEMS[item_id] = item
    return {"id": item_id, **item.dict()}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in ITEMS:
        raise HTTPException(status_code=404, detail="Item not found")
    ITEMS[item_id] = item
    return {"id": item_id, **item.dict()}


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in ITEMS:
        raise HTTPException(status_code=404, detail="Item not found")
    del ITEMS[item_id]
    return None
