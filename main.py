from predict import predict_disease
from retrieval import find_similar_images
from visualization import show_processing, show_similar_images

from tkinter import Tk
from tkinter.filedialog import askopenfilename

import os


Tk().withdraw()

image_path = askopenfilename(
    title="Select Skin Image",
    filetypes=[("Image Files","*.jpg *.jpeg *.png")]
)


if image_path:

    print("Selected Image:", os.path.basename(image_path))


    prediction, probs, classes, img, blur, gray, edges, lesion, boundary, heatmap, overlay, features = predict_disease(image_path)


    print("\nPredicted Disease:", prediction)

    print("\nConfidence:")

    for c,p in zip(classes,probs):

        print(c,"→",round(p*100,2),"%")


    show_processing(img, blur, gray, edges, lesion, boundary, heatmap, overlay)


    similar = find_similar_images(features)

    show_similar_images(similar)

else:

    print("No image selected")