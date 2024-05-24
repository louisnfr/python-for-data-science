import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """loads an image"""
    try:
        img = Image.open(path)
        img = img.convert("RGB")
        img = np.array(img)
        print("The shape of the image is:", img.shape)
        return img
    except Exception as e:
        print("Error:", e)
        return np.array([])
