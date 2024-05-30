from S1E9 import Character


class Baratheon(Character):
    """baratheon class"""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """init baratheon"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hair = "dark"

    def __str__(self) -> str:
        """baratheon str override"""
        return f"{self.first_name} {self.family_name}"

    def __repr__(self) -> str:
        """baratheon repr override"""
        return self.__str__()

    def die(self) -> None:
        """baratheon dies"""
        self.is_alive = False


class Lannister(Character):
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """init lannister"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hair = "light"

    def __str__(self) -> str:
        """lannister str override"""
        return f"{self.first_name} {self.family_name}"

    def __repr__(self) -> str:
        """baratheon repr override"""
        return self.__str__()

    def die(self) -> None:
        """lannister dies"""
        self.is_alive = False

    @staticmethod
    def create_lannister(first_name: str, is_alive: bool) -> Character:
        return Lannister(first_name, is_alive)
