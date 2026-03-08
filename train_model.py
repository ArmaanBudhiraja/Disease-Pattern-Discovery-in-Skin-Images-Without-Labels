import os
import numpy as np
import joblib
from tqdm import tqdm

from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from preprocessing import preprocess_image
from segmentation import segment_lesion
from feature_extraction import extract_features


# =========================
# Dataset path
# =========================

dataset_path = "dataset/train"


features = []
labels = []
image_paths = []


print("\nStarting dataset processing...\n")


# =========================
# Load dataset images
# =========================

for disease in os.listdir(dataset_path):

    disease_folder = os.path.join(dataset_path, disease)

    if not os.path.isdir(disease_folder):
        continue

    print(f"Processing class: {disease}")

    for img_name in tqdm(os.listdir(disease_folder)):

        path = os.path.join(disease_folder, img_name)

        try:

            img, _, _, _ = preprocess_image(path)

            lesion, _ = segment_lesion(img)

            f = extract_features(lesion)

            features.append(f)

            labels.append(disease)

            image_paths.append(path)

        except Exception as e:

            print("Skipping image:", path)


features = np.array(features)

print("\nTotal training samples:", len(features))


# =========================
# Feature Scaling
# =========================

scaler = StandardScaler()

features_scaled = scaler.fit_transform(features)


# =========================
# Train SVM model
# =========================

print("\nTraining SVM classifier...\n")

model = SVC(kernel="rbf", probability=True)

model.fit(features_scaled, labels)


# =========================
# Save model + scaler
# =========================

joblib.dump(model, "model.pkl")

joblib.dump(scaler, "scaler.pkl")


# =========================
# Save retrieval database
# =========================

joblib.dump(features_scaled, "feature_database.pkl")

joblib.dump(image_paths, "image_paths.pkl")


print("\nTraining complete!\n")

print("Saved files:")
print("model.pkl")
print("scaler.pkl")
print("feature_database.pkl")
print("image_paths.pkl")