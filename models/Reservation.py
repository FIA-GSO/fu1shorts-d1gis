from dataclasses import dataclass
from datetime import datetime

@dataclass
class Reservation:
    day: datetime
    time_from: datetime
    time_to: datetime
    table_number: int
    _id: int
    _pin: int
