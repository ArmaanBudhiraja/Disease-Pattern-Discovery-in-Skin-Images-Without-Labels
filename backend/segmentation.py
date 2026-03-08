import cv2
import numpy as np


def segment_lesion(image):

    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    L, A, B = cv2.split(lab)

    blur = cv2.GaussianBlur(A, (5, 5), 0)

    _, thresh = cv2.threshold(
        blur,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    kernel = np.ones((5, 5), np.uint8)

    clean = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    mask = cv2.morphologyEx(clean, cv2.MORPH_OPEN, kernel)

    lesion = cv2.bitwise_and(image, image, mask=mask)

    return lesion, mask


def draw_lesion_boundary(image, mask):

    contour_img = image.copy()

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)

    return contour_img