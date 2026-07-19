from fastapi import FastAPI, status

from pydantic import BaseModel

app = FastAPI()

class PlanetCreate(BaseModel):
    name: str
    fun_fact: str

planets = [
    {"id": 1,
    "name": "Saturn",
    "fun_fact": "Saturn's avg density is lower than water, so it would float, if thrown into a big enough ocean"    
          }
]

def get_next_planet_id():
    existing_ids = [planet["id"] for planet in planets]
    return max(existing_ids, default=0) + 1

@app.get("/")
def root():
    return {"message" : "Big Bang was actually a White Hole"}

@app.get("/planets")
def get_planets():
    return planets

@app.get("/planets/{planet_id}")
def get_planet(planet_id: int):
    for planet in planets:
        if planet["id"] == planet_id:
            return planet
        
    return {"error": "Planet not found"}

@app.post("/planets", status_code=status.HTTP_201_CREATED)
def create_planet(planet_data: PlanetCreate):
    
    new_planet = {
        "id": get_next_planet_id(),
        "name": planet_data.name,
        "fun_fact": planet_data.fun_fact
    }

    planets.append(new_planet)

    return new_planet

 # still a long way to go but the patterns are surely reinforcing
