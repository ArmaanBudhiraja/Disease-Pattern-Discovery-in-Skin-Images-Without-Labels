import joblib

from preprocessing import preprocess_image
from segmentation import segment_lesion, draw_lesion_boundary
from feature_extraction import extract_features
from explainability import generate_heatmap


model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")


def predict_disease(image_path):

    img, blur, gray, edges = preprocess_image(image_path)

    lesion, mask = segment_lesion(img)

    boundary = draw_lesion_boundary(img, mask)

    heatmap, overlay = generate_heatmap(lesion)

    features = extract_features(lesion)

    features = scaler.transform([features])

    prediction = model.predict(features)[0]

    probabilities = model.predict_proba(features)[0]

    classes = model.classes_

    return prediction, probabilities, classes, img, blur, gray, lesion, boundary, heatmap, overlay, features