import joblib

from backend.preprocessing import preprocess_image
from backend.segmentation import segment_lesion, draw_lesion_boundary
from backend.feature_extraction import extract_features
from backend.explainability import generate_heatmap

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")


def predict_disease(image_path):

    img, blur, gray = preprocess_image(image_path)

    lesion, mask = segment_lesion(img)

    boundary = draw_lesion_boundary(img, mask)

    heatmap, overlay = generate_heatmap(img)

    features = extract_features(lesion)

    features_scaled = scaler.transform([features])

    prediction = model.predict(features_scaled)[0]

    probabilities = model.predict_proba(features_scaled)[0]

    classes = model.classes_

    return prediction, probabilities, classes, img, blur, gray, lesion, boundary, heatmap, overlay, features_scaled