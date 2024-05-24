import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def display_image(img: np.ndarray) -> None:
    """displays an image"""
    try:
        fig = plt.figure()
        fig.add_subplot(2, 2, 1)
        plt.imshow(img)
        plt.axis("off")
        plt.title("Inverted Image")
        fig.add_subplot(2, 2, 2)
        plt.imshow(img)
        plt.show()
    except Exception as e:
        print("Error:", e)


def ft_invert(img: np.ndarray) -> np.ndarray:
    """inverts an image"""
    try:
        img = 255 - img
        return img
    except Exception as e:
        print("Error:", e)
        return np.ndarray([])


def main():
    """main function"""
    try:
        img = ft_load("landscape.jpg")
        display_image(ft_invert(img))
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
