# FastAPI Notes 

A small learning project for understanding FastAPI fundamentals: routes, HTTP methods, path parameters, request bodies, JSON responses, and automatic API documentation.

## Goal

Learn how a Python function becomes an API endpoint.

This project introduces:

HTTP request -> FastAPI endpoint -> Python function -> JSON response

## Roadmap

- [x] Create basic FastAPI project structure
- [x] Install FastAPI
- [x] Create first `FastAPI()` app instance
- [x] Add root endpoint: `GET /`
- [x] Learn how to run the development server
- [x] Open automatic docs at `/docs`
- [x] Add in-memory notes list
- [x] Add endpoint to list notes: `GET /notes`
- [x] Add endpoint to get one note by ID: `GET /notes/{note_id}`
- [x] Add request body model with Pydantic
- [x] Add endpoint to create note: `POST /notes`
- [ ] Add endpoint to update note: `PUT /notes/{note_id}`
- [ ] Add endpoint to delete note: `DELETE /notes/{note_id}`
- [ ] Add basic error handling with `HTTPException`
- [ ] Add simple input validation through Pydantic
