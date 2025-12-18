from datetime import date, timedelta


class Reservation:
    day: date
    time_from: timedelta
    time_to: timedelta
    table_number: int
    id: int
    pin: int
