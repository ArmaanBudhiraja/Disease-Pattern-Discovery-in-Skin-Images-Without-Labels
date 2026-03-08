import cv2
import numpy as np


def generate_heatmap(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # compute gradients
    grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    magnitude = cv2.magnitude(grad_x, grad_y)

    magnitude = cv2.normalize(
        magnitude,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    ).astype(np.uint8)

    heatmap = cv2.applyColorMap(magnitude, cv2.COLORMAP_JET)

    overlay = cv2.addWeighted(
        image,
        0.6,
        heatmap,
        0.4,
        0
    )

    return heatmap, overlay