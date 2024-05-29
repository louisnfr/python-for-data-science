import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


class ImageObject:
    def __init__(self, img: np.ndarray, title: str):
        self.img = img
        self.title = title


def display_images(images: list[ImageObject]) -> None:
    """displays an image"""
    try:
        f, axs = plt.subplots(1, len(images))
        for i, image in enumerate(images):
            axs[i].imshow(image.img)
            axs[i].set_title(image.title)
            axs[i].axis("off")
        plt.show()
    except Exception as e:
        print("Error:", e)


def ft_invert(img: np.ndarray) -> np.ndarray:
    """inverts color of an image"""
    try:
        return 255 - img
    except Exception as e:
        print("Error:", e)
        return np.ndarray([])


def ft_red(img: np.ndarray) -> np.ndarray:
    """returns only red channel of an image"""
    try:
        red = img.copy()
        red[:, :, 1] = 0
        red[:, :, 2] = 0
        return red
    except Exception as e:
        print("Error:", e)
        return np.ndarray([])


def ft_blue(img: np.ndarray) -> np.ndarray:
    """returns only blue channel of an image"""
    try:
        blue = img.copy()
        blue[:, :, 0] = 0
        blue[:, :, 1] = 0
        return blue
    except Exception as e:
        print("Error:", e)
        return np.ndarray([])


def ft_green(img: np.ndarray) -> np.ndarray:
    """returns only green channel of an image"""
    try:
        green = img.copy()
        green[:, :, 0] = 0
        green[:, :, 2] = 0
        return green
    except Exception as e:
        print("Error:", e)
        return np.ndarray([])


def ft_grey(img: np.ndarray) -> np.ndarray:
    """converts rgb to grey"""
    try:
        copy = img.copy()
        redC = copy[:, :, 0] / 3
        greenC = copy[:, :, 1] / 3
        blueC = copy[:, :, 2] / 3
        grey = redC + greenC + blueC
        copy[:, :, 0] = grey
        copy[:, :, 1] = grey
        copy[:, :, 2] = grey
        return copy
    except Exception as e:
        print("Error:", e)
        return np.ndarray([])


def main():
    """main function"""
    try:
        images: list[ImageObject] = []
        original = ft_load("landscape.jpg")
        images.append(ImageObject(original, "original"))
        images.append(ImageObject(ft_invert(original), "inverted"))
        images.append(ImageObject(ft_red(original), "red"))
        images.append(ImageObject(ft_green(original), "green"))
        images.append(ImageObject(ft_blue(original), "blue"))
        images.append(ImageObject(ft_grey(original), "grey"))
        display_images(images)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
