from fastapi import FastAPI, UploadFile, File
import shutil
import os
import uuid
import cv2
import base64

from predict import predict_disease
from retrieval import find_similar_images


app = FastAPI(title="Skin Disease Detection API")


UPLOAD_DIR = "temp_uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


def encode_image(image):

    _, buffer = cv2.imencode(".jpg", image)

    return base64.b64encode(buffer).decode("utf-8")


@app.post("/predict")

async def predict(file: UploadFile = File(...)):

    filename = f"{uuid.uuid4()}.jpg"

    path = os.path.join(UPLOAD_DIR, filename)

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)


    prediction, probs, classes, img, blur, gray, lesion, boundary, heatmap, overlay, features = predict_disease(path)


    similar = find_similar_images(features)


    similar_images = []

    for p in similar:

        image = cv2.imread(p)

        similar_images.append(encode_image(image))


    result = {

        "prediction": prediction,

        "probabilities": {
            c: float(p) for c,p in zip(classes,probs)
        },

        "processing_images": {

            "original": encode_image(img),

            "blur": encode_image(blur),

            "grayscale": encode_image(gray),

            "lesion": encode_image(lesion),

            "boundary": encode_image(boundary),

            "heatmap": encode_image(overlay)

        },

        "similar_images": similar_images

    }


    return result