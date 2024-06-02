class calculator:
    """A class to perform vector operations."""

    @staticmethod
    def dotproduct(v1: list[float], v2: list[float]) -> None:
        """multiply two vectors"""
        result = 0
        for i, _ in enumerate(v1):
            result += v1[i] * v2[i]
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(v1: list[float], v2: list[float]) -> None:
        """add two vectors"""
        result: list[float] = []
        for i, _ in enumerate(v1):
            result.append(float(v1[i] + v2[i]))
        print(f"Add vector is: {result}")

    @staticmethod
    def sous_vec(v1: list[float], v2: list[float]) -> None:
        """subtract two vectors"""
        result: list[float] = []
        for i, _ in enumerate(v1):
            result.append(float(v1[i] - v2[i]))
        print(f"Sous vector is: {result}")
