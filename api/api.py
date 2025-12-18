from fastapi import FastAPI

import repository

app = FastAPI()
repo = repository.Repository()

@app.get("/tische")
def get_freie_tische():
    return repo.getFreieTische()


@app.post("/reservierungen")
def post_reservierungen():
    return "reservierungen"


@app.get("/reservierungen")
def get_reservierungen():
    return "reservierungen"


@app.delete("/reservierungen/{res_id}")
def delete_reservierungen(res_id: int):
    return "reservierungen"