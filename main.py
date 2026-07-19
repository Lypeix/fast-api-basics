from fastapi import FastAPI, status # imports the FastAPI class from the fastapi library
                                    # imports status which provides readable names for HTTP status-code numbers

from pydantic import BaseModel # imports BaseModel class from pydantic
                               # FastAPI uses pydantic models to parse and validate incoming data
from helpers import get_next_note_id

app = FastAPI() # creates the object that stores all routes/endpoints and controls the API

class NoteCreate(BaseModel):
    title: str
    content: str

notes = [ 
        
        {"id": 1,
        "title": "Plushies",
        "content": "I want to buy myself an aquarium with swimming plushies"
        }
    
    ]
    # creates in-memory list of notes, which means the notes exist only when the server is running
    # this data resets whenever server gets restarted


@app.get("/")
    # creates a GET endpoint at the root path "/"
    # if user visits http://127.0.0.1:8000/ (local server host and port), FastAPI runs the function below
    # as a decorator it connects the function below to FastAPI

def root():
    # defines the function that handles GET requests to "/"

    return {"message": "FastAPI and Swimming Plushies"}
    # returns Python dict that gets automatically converted by FastAPI into a JSON response.

@app.get("/notes")
    # GET endpoint is created at path "/notes"
    # when a GET request is sent to "/notes", FastAPI calls get_notes()

def get_notes():
    return notes
    # returns the list of dictionaries that FastAPI automatically converts into JSON

@app.get("/notes/{note_id}") # note id is path parameter: dynamic URL part that identifies a specific note, eg. GET /notes/1 makes note_id receive 1. bracers {} 
                             # braces {} are FastAPI path parameter syntax

def get_note(note_id: int): # FastAPI sends the note to note id and converts it into integer, then documents its type in /docs
    for note in notes:
        if note["id"] == note_id: # loop checks each dictionary for the matching id
            return note
        
    return {"error": "Note not found"} 

@app.post("/notes", status_code=status.HTTP_201_CREATED)
# creates a POST endpoint at "/notes"
# POST is used to send data to the API and create new resource
# status_code determines the HTTP status after successful execution
# status.HTTP_201_CREATED is readable FastAPI constant representing 201
# HTTP = Hypertext Transfer Protocol, which means: 
# a set of rules that lets clients (eg. /docs sends http request) and servers (eg. this program send back http response) communicate

def create_note(note_data: NoteCreate):
# receives the request's (/docs) JSON body as note_data
# FastAPI validates the JSON body (checks if it has correct data types and structure) using the NoteCreate pydantic model
# if validation is successful, note_data becomes a NoteCreate object

    new_note = {
        "id": get_next_note_id(notes), # calls get_next_note_id() with the notes list and stores the id
        "title": note_data.title, # accesses the validated title from NoteCreate and stores it
        "content": note_data.content # accesses the validated content from NoteCreate and stores it
    }
    # creates a python dict containing the whole new note

    notes.append(new_note)
    # adds the new note dict to in-memory notes list

    return new_note
    # returns the new note dict, which then gets converted by FastAPI into a JSON body
    # because of the status_code above, the response uses HTTP 201 Created, which means that the request suceeded and a new resource (new note) was made

@app.put("/notes/{note_id}") # creates PUT endpoint to fully update an existing resource
def update_note(note_id: int, note_data: NoteCreate):
    # FastAPI validates and converts URL note_id into integer
    # due to NoteCreate, Pydantic validates the JSON body and creates a NoteCreate object
    for note in notes:
        if note["id"] == note_id:
            note["title"] = note_data.title 
            note["content"] = note_data.content

            return note # FastAPI converts updated dict into JSON with the default status 200 OK
    
    return {"error": "Note not found"}
