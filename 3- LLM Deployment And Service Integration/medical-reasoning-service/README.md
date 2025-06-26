# FastAPI Project

This is a FastAPI project

- **Controller Layer** (`app/main.py`): Exposes a single `/value` endpoint.
- **Service Layer** (`app/service.py`): Provides the `get_value` method.

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```
3. Visit `http://127.0.0.1:8000/value` to see the response.
