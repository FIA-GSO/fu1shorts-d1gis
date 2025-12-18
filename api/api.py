from fastapi import FastAPI

app = FastAPI()

@app.get("/tische")
def get_freie_tische():
    return "tisch"


@app.post("/reservierungen")
def post_reservierungen():
    return "reservierungen"


@app.get("/reservierungen")
def get_reservierungen():
    return "reservierungen"


@app.delete("/reservierungen/{res_id}")
def delete_reservierungen(res_id: int):
    return "reservierungen"