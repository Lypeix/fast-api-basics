from fastapi import FastAPI # imports the FastAPI class from the fastapi library
                            

app = FastAPI() # creates the object that stores all routes/endpoints and controls the API

notes = [ 
    {"id": 1, "title": "Plushies", "Content": "I want to buy myself an aquarium with swimming plushies"}
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
        if note[id] == note_id: # loop checks for the matching
            return note
        
    return {"error": "Note not found"} from fastapi import FastAPI # imports the FastAPI class from the fastapi library
                            

app = FastAPI() # creates the object that stores all routes/endpoints and controls the API

notes = [ 
    {"id": 1, "title": "Plushies", "Content": "I want to buy myself an aquarium with swimming plushies"}
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

@app.get("/notes/{note_id}") 
# note id is path parameter: dynamic URL part that identifies a specific note, eg. GET /notes/1 makes note_id receive 1.
# braces {} are FastAPI path parameter syntax

def get_note(note_id: int): 
  # FastAPI validates and converts note_id into inter, then documents its type in /docs
    
  for note in notes:
        if note["id"] == note_id: 
            return note
        
    return {"error": "Note not found"} 
