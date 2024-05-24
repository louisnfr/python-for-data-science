import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def zoom(img: np.ndarray) -> np.ndarray:
    """slices an image"""
    try:
        # return img
        return img[:900, :600, :]
    except Exception as e:
        print("Error:", e)
        return np.array([])


def display_image(img: np.ndarray) -> None:
    """displays an image"""
    try:
        plt.imshow(img, cmap="gray")
        plt.show()
    except Exception as e:
        print("Error:", e)


def main():
    """main function"""
    img = ft_load("animal.jpeg")
    zoomed_img = zoom(img)
    display_image(zoomed_img)


if __name__ == "__main__":
    main()
