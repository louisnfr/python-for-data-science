import numpy as np


def slice_me(family: list[list[float]], start: int, end: int) -> list[float]:
    """slice_me returns a slice of a 2D array"""
    try:
        arr = np.array(family)
        print("my shape is:", arr.shape)
        print("my new shape is:", arr[start:end].shape)
    except Exception as e:
        print(e)
        return []
    return arr[start:end].tolist()
