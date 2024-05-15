import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """slice_me returns a slice of a 2D array"""
    try:
        arr = np.array(family)
        print("my shape is:", arr.shape)
        print("my new shape is:", arr[start:end].shape)
    except ValueError as e:
        print(e)
        return None
    return arr[start:end]
