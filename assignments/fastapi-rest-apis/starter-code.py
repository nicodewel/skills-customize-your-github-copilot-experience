from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Item API")

items = [
    {"id": 1, "name": "Keyboard", "done": False},
    {"id": 2, "name": "Mouse", "done": True},
]


class Item(BaseModel):
    name: str
    done: bool = False


@app.get("/items")
def get_items():
    """Return all items."""
    return items


@app.post("/items")
def create_item(item: Item):
    """Create a new item and return it."""
    new_item = {
        "id": len(items) + 1,
        "name": item.name,
        "done": item.done,
    }
    items.append(new_item)
    return new_item


# Challenge: add a GET /items/{item_id} endpoint
# Bonus: add a PUT or DELETE endpoint for item updates
