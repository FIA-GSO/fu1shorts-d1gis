from fastapi import FastAPI

import repository
from models.Reservation import Reservation

app = FastAPI()
repo = repository.Repository()

@app.get("/tische")
def get_freie_tische():
    return repo.getFreieTische()


@app.post("/reservierungen")
def post_reservierungen(reservation: Reservation):
    return reservation


@app.get("/reservierungen")
def get_reservierungen():
    return repo.getReservations()


@app.delete("/reservierungen/{res_id}")
def delete_reservierungen(res_id: int):
    return "reservierungen"