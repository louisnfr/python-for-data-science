import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def display_image(img: np.ndarray) -> None:
    """displays an image"""
    try:
        plt.imshow(img, cmap="gray")
        plt.show()
    except Exception as e:
        print("Error:", e)


def rotate_image(img: np.ndarray) -> np.ndarray:
    """rotates an image"""
    try:
        tr = [[img[j][i] for j in range(len(img))] for i in range(len(img))]
        return np.array(tr)
    except Exception as e:
        print("Error:", e)
        return np.ndarray([])


def main():
    """main function"""
    try:
        img = ft_load("animal.jpeg")
        print(img)
        transposed = rotate_image(img[200:500, 500:800])
        print("New shape after transpose:", transposed.shape[:2])
        print(transposed)
        display_image(transposed)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
