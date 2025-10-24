"""Starter code: small FastAPI app
Run with:
    pip install -r requirements.txt
    uvicorn starter_code:app --reload
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Mini TODO API")

class Item(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    done: bool = False

# In-memory storage
_items = {}
_next_id = 1

@app.get("/items")
def list_items():
    return list(_items.values())

@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = _items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", status_code=201)
def create_item(item: Item):
    global _next_id
    item.id = _next_id
    _items[_next_id] = item.dict()
    _next_id += 1
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    stored = _items.get(item_id)
    if not stored:
        raise HTTPException(status_code=404, detail="Item not found")
    updated = item.dict()
    updated['id'] = item_id
    _items[item_id] = updated
    return updated

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id in _items:
        del _items[item_id]
        return
    raise HTTPException(status_code=404, detail="Item not found")
