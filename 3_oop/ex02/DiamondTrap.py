from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """init king"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color: str) -> None:
        """set eyes color"""
        self.eyes = color

    def set_hair(self, color: str) -> None:
        """set hair color"""
        self.hair = color

    def get_eyes(self) -> str:
        """get eyes color"""
        return self.eyes

    def get_hair(self) -> str:
        """get hair color"""
        return self.hair
