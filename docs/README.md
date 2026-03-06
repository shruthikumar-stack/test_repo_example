# Test Merge Repo

A simple Python Flask application for testing the merge flow in Helix.

## Structure.

- `src/app.py` —  Flask API with user CRUD endpoints.
- `src/models.py` — Data models (User, Project, Task)
- `src/utils.py` — Utility functions (validation, hashing, pagination)

## API Endpoints

- `GET /api/users` — List all users.
- `GET /api/users/:id` — Get user by ID
- `POST /api/users` — Create a new user
- `GET /api/health` — Health check
