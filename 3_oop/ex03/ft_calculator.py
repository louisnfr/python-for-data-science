class calculator:
    def __init__(self, vector: list[float]):
        """init"""
        self.vector = vector

    def __add__(self, other: float) -> None:
        """add"""
        for i, _ in enumerate(self.vector):
            self.vector[i] += other

    def __mul__(self, other: float) -> None:
        """multiply"""
        for i, _ in enumerate(self.vector):
            self.vector[i] *= other

    def __sub__(self, other: float) -> None:
        """multiply"""
        for i, _ in enumerate(self.vector):
            self.vector[i] -= other

    def __truediv__(self, other: float) -> None:
        """multiply"""
        if other == 0:
            raise ZeroDivisionError("Error: division by zero")
        for i, _ in enumerate(self.vector):
            self.vector[i] /= other
