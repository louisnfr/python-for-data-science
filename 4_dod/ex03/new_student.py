import random
import string
from dataclasses import dataclass, field


def generate_id():
    """generates id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student data class"""

    name: str
    surname: str
    id: str = field(init=False, default=generate_id())
    login: str = field(init=False)
    active: bool = field(default=True)

    def __post_init__(self):
        self.login = "".join([self.name[0], self.surname]).lower()
