# DEVLOG

## DAY 1 - STARTING THE PROJECT (17.07.2026)
### Session 1 (~50mins):
- Installed FastAPI
- Created first FastAPI app instance
- Added root endpoint with `@app.get("/")`
- Added first JSON response with a Python dict
- Added in-memory notes list
- Added `/notes` endpoint returning the notes list as JSON
- Added comments explaining the concepts, however my understanding is still scarce. I am leaving the deeper theory for tomorrow
- Ran the app using py -m uvicorn main:app --reload

## DAY 2 OF PROGRESS (18.07.2026)
### Session 1 (~40mins)
- Reviewed concepts from Day 1 and basic API flow
- Checked the automatic documentation at /docs
- Added endpoint to get one note by id
- Added comments explaining the process

### Session 2 (~60mins)
- Added helpers.py containing get_next_note_id(notes)
- Passed the notes into the helper to avoid circular import
- Added `NoteCreate` Pydantic model for note data
- Added `POST /notes` for creating new notes
- Added automatic ID generation based on the highest existing note id
- Added new notes to the in-memory list
- Made successful creation responses use HTTP 201 Created
- Studied a bunch of theory regarding HTTP, status codes, POST, pydantic, JSON bodies and API request-response flow 
- Added comments explaining every addition
- I need way more practice with these new things
