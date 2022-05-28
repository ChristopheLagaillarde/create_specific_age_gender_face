# Program : image_resize
# Description : Allow to resize an image
# Date : 26/05/22
# Author : Christophe Lagaillarde
# Version : 1.0

import cv2
import numpy as np


def image_resize(image: np.ndarray, width: int = None, height: int = None, inter: int = cv2.INTER_AREA) -> np.ndarray:

    # variables
    current_width: int
    current_height: int
    dim: tuple
    ratio: float

    (current_height, current_width) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        ratio = height / float(current_height)
        dim = (int(current_width * ratio), height)
    else:
        ratio = width / float(current_width)
        dim = (width, int(current_height * ratio))

    return cv2.resize(image, dim, interpolation=inter)
