import joblib
import numpy as np

database = joblib.load("feature_database.pkl")
image_paths = joblib.load("image_paths.pkl")


def find_similar_images(query_feature, top_k=5):

    distances = np.linalg.norm(database - query_feature, axis=1)

    indices = np.argsort(distances)[:top_k]

    results = []

    for i in indices:
        results.append(image_paths[i])

    return results