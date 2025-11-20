from fastapi import FastAPI
import api.crud as crud
from pydantic import BaseModel

app = FastAPI()

class Short(BaseModel):
    url: str

@app.get("/v1/shorts")
def read_all_shorts():
    return crud.read_all()

@app.get("/v1/short/{short_id}")
def read_short(short_id: int):
    return crud.read_short(short_id)

@app.get("/v1/shorts/random")
def read_random_short():
    return crud.read_short_random()

@app.delete("/v1/short/{short_id}")
def delete_short(short_id: int):
    return crud.delete_short(short_id)

@app.post("/v1/short/")
def add_short(short: Short):
    return crud.create_short(short.url)