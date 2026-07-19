from fastapi import FastAPI, status, HTTPException

from pydantic import BaseModel, Field

app = FastAPI()

class PlanetCreate(BaseModel):
    name: str = Field(min_length=1, max_length=20)
    fun_fact: str = Field(min_length=5, max_length=200)

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
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Planet not found"
    )

    

@app.post("/planets", status_code=status.HTTP_201_CREATED)
def create_planet(planet_data: PlanetCreate):
    
    new_planet = {
        "id": get_next_planet_id(),
        "name": planet_data.name,
        "fun_fact": planet_data.fun_fact
    }

    planets.append(new_planet)

    return new_planet

@app.put("/planets/{planet_id}")
def update_planet(planet_id: int, planet_data: PlanetCreate):

    for planet in planets:
        if planet["id"] == planet_id:
            planet["name"] = planet_data.name
            planet["fun_fact"] = planet_data.fun_fact

            return planet

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Planet not found"
    )


@app.delete("/planets/{planet_id}")
def delete_planet(planet_id: int):
    for idx, planet in enumerate(planets):
        if planet["id"] == planet_id:
            obliterated_planet = planets.pop(idx)

            return {
                "message": "Imperator Palpatine, the planet was successfuly destroyed",
                "obliterated_planet": obliterated_planet
            }
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Planet not found"
    )

 # still a long way to go but the patterns are surely reinforcing
