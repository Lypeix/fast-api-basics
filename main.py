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
