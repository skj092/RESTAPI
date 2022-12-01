# REST API with FastAPI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# list of items
items = [
    {"id": 1, "name": "item1"},
    {"id": 2, "name": "item2"},
    {"id": 3, "name": "item3"},
]

@app.get("/")
def index():
    data = "<html><body><h1>REST API with FastAPI</h1><h3>you can test get method by /items /items/id (1<=id<=3)</h3><h3>You can add an item with /items update and items with \
    /items/id delete an item with /items/id </h3></body></html>"
    return HTMLResponse(content=data, status_code=200)

# GET /items
@app.get("/items")
def get_items():
    return items

# GET /items/{item_id}
@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"id": None, "name": None}

# POST /items
@app.post("/items")
def create_item(item: dict):
    items.append(item)
    return items

# PUT /items/{item_id}
@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    for i, _item in enumerate(items):
        if _item["id"] == item_id:
            items[i] = item
            return item
    return {"id": None, "name": None}

# DELETE /items/{item_id}
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i, item in enumerate(items):
        if item["id"] == item_id:
            del items[i]
            return {"id": item_id, "name": "deleted"}
    return {"id": None, "name": None}