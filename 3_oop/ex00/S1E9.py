from abc import ABC, abstractmethod


class Character(ABC):
    """Character class"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """init"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """abstract die method"""
        pass


class Stark(Character):
    """Stark class"""

    def die(self):
        """die method"""
        self.is_alive = False

    pass
