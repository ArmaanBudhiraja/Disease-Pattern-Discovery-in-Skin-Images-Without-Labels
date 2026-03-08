# Disease Pattern Discovery in Skin Images Without Labels
A machine learning and computer vision system for discovering dermatological disease patterns in skin images without relying on annotated datasets or deep learning models.

This project uses classical image processing techniques, feature extraction, and machine learning to analyze skin lesions, identify patterns, and retrieve visually similar cases from a dataset.

## Overview

Skin disease detection often requires large labeled datasets and deep neural networks, which are expensive and time-consuming to create.
This project explores an alternative approach by using:
- Color analysis
- Texture analysis
- Structural pattern extraction

to detect and classify dermatological patterns without needing labeled training data for segmentation or deep learning models.
The system also provides visual explainability and case-based retrieval to help understand predictions.

## Key Features

Image preprocessing and enhancement

Lesion segmentation using color space analysis

Feature extraction using:

- Color histogram

- GLCM texture features

- Local Binary Patterns (LBP)

Machine learning classification using SVM

Explainability via heatmap visualization

Case-based retrieval of similar images from the dataset

Interactive web interface for uploading and analyzing images

## System Architecture

User Upload Image
        ↓
Image Preprocessing
        ↓
Lesion Segmentation
        ↓
Feature Extraction
(Color + Texture + Structure)
        ↓
Feature Scaling
        ↓
SVM Classification
        ↓
Explainability Heatmap
        ↓
Similar Image Retrieval
        ↓
Results Displayed in Web Interface