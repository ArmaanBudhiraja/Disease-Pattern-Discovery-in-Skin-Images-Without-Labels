import cv2
import numpy as np
from skimage.feature import graycomatrix, graycoprops, local_binary_pattern


def extract_features(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    hist = cv2.calcHist(
        [image],
        [0, 1, 2],
        None,
        [16, 16, 16],
        [0, 256, 0, 256, 0, 256]
    )

    hist = cv2.normalize(hist, hist).flatten()

    glcm = graycomatrix(
        gray,
        [1],
        [0],
        256,
        symmetric=True,
        normed=True
    )

    contrast = graycoprops(glcm, 'contrast')[0, 0]
    energy = graycoprops(glcm, 'energy')[0, 0]
    homogeneity = graycoprops(glcm, 'homogeneity')[0, 0]

    texture = [contrast, energy, homogeneity]

    lbp = local_binary_pattern(gray, 8, 1, "uniform")

    lbp_hist, _ = np.histogram(
        lbp.ravel(),
        bins=10,
        range=(0, 10)
    )

    lbp_hist = lbp_hist.astype("float")
    lbp_hist /= (lbp_hist.sum() + 1e-6)

    return np.hstack([hist, texture, lbp_hist])