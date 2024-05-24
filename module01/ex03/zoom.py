import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def display_image(img: np.ndarray) -> None:
    """displays an image"""
    try:
        x, y, z = img.shape
        if x < 300 or y < 300:
            raise ValueError("Image is too small to display")
        plt.imshow(img, cmap="gray")
        plt.show()
    except Exception as e:
        print("Error:", e)


def main():
    """main function"""
    try:
        img = ft_load("animal.jpeg")
        print(img)
        zoomed_img = img[200:500, 500:800, :1]
        print("New shape after slicing:", zoomed_img.shape)
        print(zoomed_img)
        display_image(zoomed_img)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
