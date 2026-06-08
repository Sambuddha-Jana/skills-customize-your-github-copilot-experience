# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small RESTful API using the FastAPI framework. Students will implement CRUD endpoints, use Pydantic models for validation, and run the app with automatic API docs.

## 📝 Tasks

### 🛠️ Task 1 — Create the API

#### Description
Implement a simple item management API with the following endpoints: list items, get item by id, create item, update item, and delete item.

#### Requirements
Completed program should:

- Expose a `GET /items` endpoint that returns a list of items.
- Expose a `GET /items/{item_id}` endpoint that returns a single item or 404 when not found.
- Expose a `POST /items` endpoint that accepts a JSON body and returns the created item with validation.
- Expose `PUT /items/{item_id}` and `DELETE /items/{item_id}` endpoints to update and remove items.
- Use Pydantic models for request and response schemas.

### 🛠️ Task 2 — Validation & Docs

#### Description
Add validations to ensure required fields are present and types are correct. Familiarize yourself with the automatic interactive docs provided by FastAPI.

#### Requirements

- Define Pydantic models with types and constraints (e.g., `name: str`, `price: float`).
- Verify interactive docs at `/docs` and `/redoc` when the server is running.

### 🛠️ Task 3 — (Optional) Persistence & Tests

#### Description
For extra practice, persist data to a file or an in-memory store across requests and add unit tests for the endpoints.

#### Requirements

- Add simple persistence (JSON file or TinyDB) or explain how to integrate a real DB.
- Provide a few pytest tests exercising the main endpoints.

## Setup & Run

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the app with Uvicorn:

```bash
uvicorn starter-code:app --reload
```

3. Open interactive docs:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Example requests

Create an item:

```bash
curl -X POST "http://127.0.0.1:8000/items" -H "Content-Type: application/json" -d '{"name":"Widget","price":9.99}'
```

Get list of items:

```bash
curl http://127.0.0.1:8000/items
```

Update an item:

```bash
curl -X PUT "http://127.0.0.1:8000/items/1" -H "Content-Type: application/json" -d '{"name":"Updated","price":12.5}'
```

Delete an item:

```bash
curl -X DELETE http://127.0.0.1:8000/items/1
```

---

See `starter-code.py` for a minimal working example to get started.
