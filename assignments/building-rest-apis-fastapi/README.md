Building REST APIs with FastAPI

Overview

This assignment teaches students how to design and implement RESTful APIs using the FastAPI framework. Students will build a small API, add request validation, document endpoints with OpenAPI, and write simple tests.

Learning objectives

- Understand FastAPI basics and ASGI servers
- Create GET/POST/PUT/DELETE endpoints
- Use Pydantic models for validation
- Explore automatic OpenAPI docs
- Write basic unit tests for endpoints

Prerequisites

- Basic Python (functions, classes, lists, dicts)
- Python 3.9+ installed

Setup

1. Create a virtual environment:

   python3 -m venv .venv
   source .venv/bin/activate

2. Install dependencies:

   pip install -r requirements.txt

3. Run the app locally:

   uvicorn starter_code:app --reload

Tasks

1. Explore the starter FastAPI app in `starter-code.py`.
2. Implement CRUD endpoints for a simple resource (e.g., items or notes).
3. Add Pydantic models for request/response validation.
4. Ensure the API has clear path and query parameters handling.
5. Use automated docs at `/docs` and `/redoc` to verify endpoints.
6. Write at least two tests that exercise main endpoints.

Submission

- Push your code to the assignment folder and ensure `starter-code.py` runs.
- Include any tests and a short `README.md` with instructions to run them.

Testing

- Install test dependencies with the project requirements.
- Run tests with:

   pytest
