from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI(title="FastAPI Route Protection")


# Example in-memory API keys and roles for classroom practice.
API_KEYS = {
    "student-key-123": "student",
    "admin-key-456": "admin",
}


items = [
    {"id": 1, "name": "Notebook"},
    {"id": 2, "name": "Marker"},
]


def get_role(x_api_key: str | None = Header(default=None)) -> str:
    if not x_api_key or x_api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return API_KEYS[x_api_key]


def require_admin(role: str = Depends(get_role)) -> str:
    if role != "admin":
        raise HTTPException(status_code=403, detail="Admin role required")
    return role


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def list_items(role: str = Depends(get_role)):
    return {"role": role, "items": items}


@app.post("/items")
def create_item(name: str, role: str = Depends(get_role)):
    new_id = max(item["id"] for item in items) + 1 if items else 1
    new_item = {"id": new_id, "name": name}
    items.append(new_item)
    return {"role": role, "item": new_item}


@app.delete("/admin/items/{item_id}")
def delete_item(item_id: int, role: str = Depends(require_admin)):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            deleted = items.pop(index)
            return {"role": role, "deleted": deleted}
    raise HTTPException(status_code=404, detail="Item not found")
