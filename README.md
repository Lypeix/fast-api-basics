# FastAPI Notes 

A small learning project for understanding FastAPI fundamentals: routes, HTTP methods, path parameters, request bodies, JSON responses, and automatic API documentation.

## Goal

Learn how a Python function becomes an API endpoint.

Previous projects used:

CLI input -> Python function -> SQLite -> printed output

This project introduces:

HTTP request -> FastAPI endpoint -> Python function -> JSON response

## Roadmap

- [x] Create basic FastAPI project structure
- [x] Install FastAPI
- [x] Create first `FastAPI()` app instance
- [ ] Add root endpoint: `GET /`
- [ ] Learn how to run the development server
- [ ] Open automatic docs at `/docs`
- [ ] Add in-memory notes list
- [ ] Add endpoint to list notes: `GET /notes`
- [ ] Add endpoint to get one note by ID: `GET /notes/{note_id}`
- [ ] Add request body model with Pydantic
- [ ] Add endpoint to create note: `POST /notes`
- [ ] Add endpoint to update note: `PUT /notes/{note_id}`
- [ ] Add endpoint to delete note: `DELETE /notes/{note_id}`
- [ ] Add basic error handling with `HTTPException`
- [ ] Add simple input validation through Pydantic

## Concepts Practiced

- FastAPI basics
- API endpoints/routes
- HTTP methods: `GET`, `POST`, `PUT`, `DELETE`
- Path parameters
- Request bodies
- JSON responses
- Pydantic models
- Automatic Swagger docs
- Basic API error handling
- In-memory data storage

## Planned File Structure

```text
fastapi-notes-intro/
  main.py        # FastAPI app and endpoints
  README.md      # Project documentation
  DEVLOG.md      # Learning log
