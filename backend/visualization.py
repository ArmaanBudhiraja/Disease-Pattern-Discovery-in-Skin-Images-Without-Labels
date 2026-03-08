import matplotlib.pyplot as plt
import cv2


def show_processing(img, blur, gray, lesion, boundary, heatmap, overlay):

    plt.figure(figsize=(15, 8))

    plt.subplot(2, 3, 1)
    plt.title("Original Image")
    plt.imshow(img[:, :, ::-1])
    plt.axis("off")

    plt.subplot(2, 3, 2)
    plt.title("Blurred Image")
    plt.imshow(blur[:, :, ::-1])
    plt.axis("off")

    plt.subplot(2, 3, 3)
    plt.title("Grayscale Image")
    plt.imshow(gray, cmap="gray")
    plt.axis("off")

    plt.subplot(2, 3, 4)
    plt.title("Segmented Lesion")
    plt.imshow(lesion[:, :, ::-1])
    plt.axis("off")

    plt.subplot(2, 3, 5)
    plt.title("Lesion Boundary Detection")
    plt.imshow(boundary[:, :, ::-1])
    plt.axis("off")

    plt.subplot(2, 3, 6)
    plt.title("Feature Heatmap Overlay")
    plt.imshow(overlay[:, :, ::-1])
    plt.axis("off")

    plt.tight_layout()
    plt.show()


def show_similar_images(paths):

    plt.figure(figsize=(10, 4))

    for i, path in enumerate(paths):

        img = cv2.imread(path)

        plt.subplot(1, len(paths), i + 1)

        plt.imshow(img[:, :, ::-1])

        plt.axis("off")

    plt.suptitle("Similar Images from Dataset")

    plt.show()