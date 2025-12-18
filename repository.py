from models import Table

class Repository:
    def __init__(self):
        # Platzhalter für spätere DB-Anbindung
        self.tables = [
            Table(id=1, seats=2, is_free=True),
            Table(id=2, seats=4, is_free=False),
            Table(id=3, seats=6, is_free=True),
        ]

    def getFreieTische(self) -> list[Table]:
        return self.tables
