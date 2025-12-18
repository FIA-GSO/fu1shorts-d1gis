from dataclasses import dataclass
from datetime import date, timedelta

@dataclass
class Reservation:
    day: date
    time_from: timedelta
    time_to: timedelta
    table_number: int
    _id: int
    _pin: int
