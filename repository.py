from datetime import datetime

from models.Reservation import Reservation
from models.Table import Table


class Repository:
    def __init__(self):
        # Platzhalter für spätere DB-Anbindung
        self.tables = [
            Table(1, 2, True),
            Table(1, 2, True),
            Table(1, 2, True),
        ]

    def getFreieTische(self) -> list[Table]:
        t = Table(1,2,True)
        return self.tables

    def getReservations(self) -> list[Reservation]:
        return [Reservation(datetime.now(), datetime.now(), datetime.now(), 3, 3, 3)]