from dataclasses import dataclass


@dataclass
class Table:
    number: int
    seats: int
    is_free: bool